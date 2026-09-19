"""MkDocs hooks for the recipe site.

Keeps every file under `recipes/` untouched:

* The homepage and tag index are generated at build time (the homepage from
  the repository README, so the README stays the single place a new recipe
  gets listed).
* Each recipe's trailing ``**Tags:** `#beef` ...`` line becomes real page
  tags for the Material tags plugin, and is dropped from the rendered page
  so the theme's tag chips are the only copy.
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


def on_files(files, config):
    """Add the generated homepage and tag index to the file collection."""
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    # README links are repo-relative (`recipes/breads/x.md`); inside docs_dir
    # they need to be relative to `recipes/` itself.
    home = readme.replace("](recipes/", "](")

    files.append(File.generated(config, "index.md", content=home))
    files.append(File.generated(config, "tags.md", content=TAGS_PAGE))
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
