# Project Context: Favorite Recipes

This repository stores personal recipes in standardized markdown format for easy viewing on GitHub.

## Recipe Formatting Specification

When given a recipe to add, Claude must format it according to this specification.

## Copyright Guidelines

**IMPORTANT:** Always reword the instructions in your own words to avoid copyright issues. Recipe ingredients cannot be copyrighted, but the specific written instructions can be. When formatting a recipe:

- Keep the same steps and techniques
- Rewrite the wording and phrasing to be original
- Maintain clarity and accuracy while using different language
- Do not copy instructions verbatim from the source

### File Location

Recipes are organized by category in `/recipes/`:
```
/recipes
  /desserts
  /mains
    /beef
    /chicken
    /pork
    /seafood
    /vegetarian
  /sides
  /appetizers
  /breakfast
  /soups
  /salads
/images
```

Filename: lowercase, hyphenated (e.g., `korean-beef-bowls.md`)

### Required Format

```markdown
# Recipe Name

> Brief description of the dish.

## Details

| | |
|-----|-----|
| **Source** | Original source or link |
| **Cuisine** | e.g., Korean, Italian |
| **Servings** | Number |
| **Prep Time** | If provided |
| **Cook Time** | If provided |
| **Total Time** | If provided |
| **Storage** | If provided |

## Ingredients

Group ingredients by component (e.g., ### Sauce, ### For Serving).
Each group uses a table with Imperial and Metric columns.

### Component Name
| Ingredient | Imperial | Metric |
|------------|----------|--------|
| Ingredient description | amount | converted amount |

### Conversion Notes
- Convert between imperial and metric for all measurements
- Use grams (g) for dry ingredients, milliliters (ml) for liquids
- Keep items like "6 cloves" or "2 cucumbers" as-is in both columns

## Instructions

Group instructions by component if the recipe has distinct parts.

### Component Name
1. Numbered steps
2. Keep steps concise and clear

## Notes

Include any tips, variations, or heat level guidance from the original recipe.
Leave this section for the user to add personal observations later.

---
**Tags:** `#tag1` `#tag2` `#tag3`
```

### Tag Guidelines

- Include cuisine type (e.g., `#korean`, `#italian`)
- Include main protein or base (e.g., `#beef`, `#chicken`, `#pasta`)
- Include meal type if relevant (e.g., `#mealprep`, `#quickmeal`)
- Include dietary notes if applicable (e.g., `#lowcarb`, `#vegetarian`)

## README Updates

**IMPORTANT:** When adding a new recipe, also update `README.md` to include a link to the new recipe.

README structure:
```markdown
# Favorite Recipes

A personal collection of recipes in standardized markdown format.

## Recipes

### Mains

#### Beef
- [Recipe Name](recipes/mains/beef/recipe-name.md)

#### Chicken
- [Recipe Name](recipes/mains/chicken/recipe-name.md)

### Desserts
- [Recipe Name](recipes/desserts/recipe-name.md)

### Sides
- [Recipe Name](recipes/sides/recipe-name.md)
```

- Add category headers (### Mains, ### Desserts, etc.) as needed
- Add subcategory headers (#### Beef, #### Chicken, etc.) under Mains
- Keep recipes alphabetized within each category
- Create new category/subcategory sections when adding the first recipe of that type
