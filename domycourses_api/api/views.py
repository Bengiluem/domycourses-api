from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .utils.scrapper import get_items

import json


@csrf_exempt  # TODO: remove
def get_recipes(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        recipes = data["recipes"] if "recipes" in data else []
        response = get_items(recipes)
        return JsonResponse(response, status=200)
    else:
        return JsonResponse({"message": f"Wrong method ({request.method})"}, 400)
