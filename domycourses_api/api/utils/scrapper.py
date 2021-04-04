import logging
from .marmiton import MarmitonScrapper, MarmitonScrapperException, MarmitonUnitCombiner, MarmitonCombinerException


def get_items(urls):
    recipes = []
    for url in urls:
        if "https://www.marmiton.org/" in url:
            logging.info(f"Getting {url}")
            try:
                recipes.append(MarmitonScrapper.parse_url(url))
            except MarmitonScrapperException:
                logging.error(f"Impossible to get {url}")
    return assemble(recipes)


def assemble(recipes):
    ingredients = {}
    for recipe in recipes:
        for ingredient_name, ingredient_details in recipe:
            if ingredient_name in ingredients:
                try:
                    combination = MarmitonUnitCombiner.combine(ingredient_details, ingredients[ingredient_name])
                    ingredients[ingredient_name]["unit"] = combination["unit"]
                    ingredients[ingredient_name]["quantity"] = combination["quantity"]
                    ingredients[ingredient_name]["complement"] += f", {ingredient_details['complement']}"
                except MarmitonCombinerException:
                    logging.error(f"Impossible to combine {ingredient_details['quantity']} {ingredient_details['unit']} with {ingredients[ingredient_name]['quantity']} {ingredients[ingredient_name]['unit']}")
            else:
                ingredients[ingredient_name] = ingredient_details
    return ingredients
