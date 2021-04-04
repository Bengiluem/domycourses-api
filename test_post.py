import requests

data = {
    "recipes": [
        "https://www.marmiton.org/recettes/recette_saute-de-veau-aux-champignons_20236.aspx",
        "https://www.marmiton.org/recettes/recette_sauce-bolognaise_24157.aspx"
    ]
}
url = "http://localhost:8000/api/recipes/"
requests.post(url, data=data)
