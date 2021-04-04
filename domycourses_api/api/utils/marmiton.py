from bs4 import BeautifulSoup
import requests


class MarmitonScrapperException(Exception):
    pass


class MarmitonCombinerException(Exception):
    pass


class MarmitonScrapper(object):

    @staticmethod
    def __clean_text(element):
        return element.text.replace("\n", "").strip()

    @staticmethod
    def parse_url(url):
        page = requests.get(url)
        bs = BeautifulSoup(page.content, 'html.parser')
        ingredient_list = bs.select('.ingredient-list .item-list__item .item-list__item')
        parsed_ingredients = {}
        try:
            for ingredient in ingredient_list:
                quantity = MarmitonScrapper.__clean_text(ingredient.find(class_='quantity'))
                unit = MarmitonScrapper.__clean_text(ingredient.find(class_='unit'))
                name = MarmitonScrapper.__clean_text(ingredient.find(class_='ingredient-name'))
                complement = MarmitonScrapper.__clean_text(ingredient.find(class_='ingredient-complement'))
                parsed_ingredients[name] = {
                    "quantity": float(quantity) if quantity != "" else None,
                    "unit": unit if unit != "" else None,
                    "complement": complement if complement != "" else None
                }
        except Exception:
            raise MarmitonScrapperException
        return parsed_ingredients


class MarmitonUnitCombiner(object):

    grammes = ['kg', 'g']
    litres = ['l', 'ml']

    @staticmethod
    def combine(value1, value2):
        if value1["unit"] == value2["unit"]:
            return {
                "unit": value1["unit"],
                "quantity": value1["quantity"] + value2["quantity"]
            }
        else:
            if value1["unit"] in MarmitonUnitCombiner.grammes and value2["unit"] in MarmitonUnitCombiner.grammes:
                units = MarmitonUnitCombiner.grammes
            elif value1["unit"] in MarmitonUnitCombiner.litres and value2["unit"] in MarmitonUnitCombiner.litres:
                units = MarmitonUnitCombiner.litres
            else:
                raise MarmitonCombinerException
            index1 = units.index(value1["unit"])
            index2 = units.index(value2["unit"])
            min_index = min(index1, index2)
            return {
                "unit": units[min_index],
                "quantity": (value1 / (1000 ^ (index1 - min_index))) + (value2 / (1000 ^ (index2 - min_index)))
            }





