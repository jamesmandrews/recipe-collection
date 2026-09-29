# Claude Code Rules

## Git Commits
- Never add `Co-Authored-By` lines to commit messages
- Never add any AI/Claude/Anthropic attribution to commits

## Recipes
- When adding a new recipe, always add it to the README.md in the appropriate category section, in alphabetical order
- All recipe files live under `recipes/` organized by category (appetizers, breads, desserts, mains, sauces, sides)
- Always translate recipes to English
- Always include both imperial and metric measurements. If a recipe only has one system, convert and add the other
- **Baked goods MUST be weighed, not measured by volume.** In any recipe that is baked (breads, cakes, cookies, pastry, biscuits, pie dough, batters, streusels, glazes), convert these ingredients to weight in **both** columns — ounces in Imperial, grams in Metric — even when the source recipe gives cups or tablespoons:
  - Flours and other milled/starchy dry goods (all-purpose, bread, cake, whole wheat, almond flour, cornmeal, cocoa powder, cornstarch, oats)
  - Sugars (granulated, brown, powdered, turbinado)
  - Butter, shortening, and other solid fats
  - Thick scoopables that pack unevenly (yogurt, sour cream, nut butter, honey, molasses, pumpkin purée)
  - Chocolate, nuts, and dried fruit
  - Leave as volume: spices, leaveners, salt, extracts, and pourable liquids (milk, water, oil, cream). Also leave anything under about 5 g as volume — it is below the resolution of most home scales — and say so in `## Notes`
  - Restate weights in the `## Instructions` body wherever an amount is repeated, e.g. "Beat the 4.8 oz (135 g) sugar..."
  - Add a `## Notes` bullet explaining that these ingredients are weighed (a scooped cup of flour can run 20% heavy)
- **All recipes MUST follow this format** (see `recipes/mains/pork/filipino-adobo-pork-ribs.md` as reference):
  1. `# Title`
  2. `> Short description` (blockquote)
  3. `## Details` — metadata in a two-column table (Source, Cuisine, Servings, Prep Time, Cook Time, etc.)
  4. `## Ingredients` — tables with columns: `Ingredient | Imperial | Metric` (never a single "Amount" column). Use `### Subsection` headings to group ingredients when needed
  5. `## Instructions` — use `### Step Name` subsection headings to group related steps
  6. `## Notes` — bullet list
  7. `---` followed by `**Tags:**` line with backtick-wrapped hashtags
