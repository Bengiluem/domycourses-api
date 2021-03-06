import logging
from .marmiton import MarmitonScrapper, MarmitonScrapperException, MarmitonUnitCombiner, MarmitonCombinerException
from ..models import Recipe


def get_items(urls):
    recipes = []
    for url in urls:
        try:
            recipe = Recipe.objects.get(url=url)
            logging.info("Successfully provided cached url "+url)
            recipes.append(recipe.content)
        except Recipe.DoesNotExist:
            if "https://www.marmiton.org/" in url:
                logging.info(f"Getting {url}")
                try:
                    recipe = MarmitonScrapper.parse_url(url)
                    recipes.append(recipe)
                    Recipe(url=url, content=recipe).save()
                    logging.info("Successfully retrieved & cached url " + url)
                except MarmitonScrapperException:
                    logging.error(f"Impossible to get {url}")
    assembly = assemble(recipes)
    for key, value in assembly.items():
        value["complement"] = ", ".join(value["complement"])
    return assembly


def assemble(recipes):
    ingredients = {}
    for recipe in recipes:
        for ingredient_name, ingredient_details in recipe.items():
            if ingredient_name in ingredients:
                try:
                    combination = MarmitonUnitCombiner.combine(ingredient_details, ingredients[ingredient_name])
                    ingredients[ingredient_name]["unit"] = combination["unit"]
                    ingredients[ingredient_name]["quantity"] = combination["quantity"]
                    if ingredient_details["complement"] is not None:
                        ingredients[ingredient_name]["complement"].add(ingredient_details["complement"])
                except MarmitonCombinerException:
                    logging.error(f"Impossible to combine {ingredient_details['quantity']} {ingredient_details['unit']} with {ingredients[ingredient_name]['quantity']} {ingredients[ingredient_name]['unit']} for ingredient {ingredient_name}")
            else:
                ingredients[ingredient_name] = {
                    "unit": ingredient_details["unit"],
                    "quantity": ingredient_details["quantity"],
                    "complement": {ingredient_details["complement"]} if ingredient_details["complement"] is not None else set()
                }
    return ingredients
