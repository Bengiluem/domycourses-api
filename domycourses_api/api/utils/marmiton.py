from bs4 import BeautifulSoup
import requests


class MarmitonScrapperException(Exception):
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
                    "quantity": quantity if quantity != "" else None,
                    "unit": unit if unit != "" else None,
                    "complement": complement if complement != "" else None
                }
        except Exception:
            raise MarmitonScrapperException
        return parsed_ingredients
