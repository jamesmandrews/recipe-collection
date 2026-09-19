"""MkDocs hooks for the recipe site.

Keeps every file under `recipes/` untouched:

* The homepage and tag index are generated at build time (the homepage from
  the repository README, so the README stays the single place a new recipe
  gets listed).
* Each recipe's trailing ``**Tags:** `#beef` ...`` line becomes real page
  tags for the Material tags plugin, and is dropped from the rendered page
  so the theme's tag chips are the only copy.
* The theme override stylesheet is generated too, so the palette that ties
  this site to jamesmandrews.com lives next to the rest of the build logic
  rather than as a stray asset inside `recipes/`.
"""

import re
from pathlib import Path

from mkdocs.plugins import event_priority
from mkdocs.structure.files import File

ROOT = Path(__file__).parent.parent

# The `---` rule plus `**Tags:**` line that closes every recipe.
TAGS_BLOCK = re.compile(r"\n+---\n+\*\*Tags:\*\*(.*?)\s*$", re.DOTALL)
TAG = re.compile(r"`#([\w-]+)`")

TAGS_PAGE = """# Tags

Browse every recipe by tag.

<!-- material/tags -->
"""

# Palette and display face borrowed from jamesmandrews.com, which links here:
# teal ink on paper in light, and the site's near-black in dark, so the header
# stops being the brightest thing on the page. Both schemes are always stated,
# the same rule the main site follows.
EXTRA_CSS = """\
@import url("https://fonts.googleapis.com/css2\
?family=Bricolage+Grotesque:opsz,wght@12..96,400..800&display=swap");

[data-md-color-scheme="default"] {
  --md-primary-fg-color:             #16665a;
  --md-primary-fg-color--light:      #1d8072;
  --md-primary-fg-color--dark:       #0f4b42;
  --md-accent-fg-color:              #16665a;
  --md-accent-fg-color--transparent: rgba(22, 102, 90, 0.10);
  --md-typeset-a-color:              #16665a;
  --md-default-bg-color:             #fafaf8;
  --md-code-bg-color:                #f1f1ed;
}

[data-md-color-scheme="slate"] {
  --md-primary-fg-color:             #101319;
  --md-primary-fg-color--light:      #171b23;
  --md-primary-fg-color--dark:       #0b0e13;
  --md-accent-fg-color:              #5fbfa9;
  --md-accent-fg-color--transparent: rgba(95, 191, 169, 0.10);
  --md-typeset-a-color:              #5fbfa9;
  --md-default-bg-color:             #101319;
  --md-default-fg-color:             #e9ebf0;
  --md-default-fg-color--light:      #98a1b4;
  --md-default-fg-color--lighter:    rgba(233, 235, 240, 0.32);
  --md-default-fg-color--lightest:   rgba(233, 235, 240, 0.14);
  --md-code-bg-color:                #171b23;
}

/* The header sits on the dark ground in slate, so it needs a seam. */
[data-md-color-scheme="slate"] .md-header {
  border-bottom: 1px solid rgba(233, 235, 240, 0.14);
}

/* Headings in the display face, tracked in like the main site's. */
.md-typeset h1,
.md-typeset h2,
.md-typeset h3 {
  font-family: "Bricolage Grotesque", var(--md-text-font-family), sans-serif;
  font-weight: 700;
}

.md-typeset h1 { letter-spacing: -0.03em; }
.md-typeset h2 { letter-spacing: -0.025em; }
.md-typeset h3 { letter-spacing: -0.02em; }
"""


def on_files(files, config):
    """Add the generated homepage, tag index and theme stylesheet."""
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    # README links are repo-relative (`recipes/breads/x.md`); inside docs_dir
    # they need to be relative to `recipes/` itself.
    home = readme.replace("](recipes/", "](")

    files.append(File.generated(config, "index.md", content=home))
    files.append(File.generated(config, "tags.md", content=TAGS_PAGE))
    files.append(
        File.generated(config, "stylesheets/extra.css", content=EXTRA_CSS)
    )
    return files


@event_priority(100)  # must run before the tags plugin reads page.meta
def on_page_markdown(markdown, page, config, files):
    match = TAGS_BLOCK.search(markdown)
    if not match:
        return markdown

    tags = TAG.findall(match.group(1))
    if tags:
        page.meta["tags"] = tags

    return markdown[: match.start()]
