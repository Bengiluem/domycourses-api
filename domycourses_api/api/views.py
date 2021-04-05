from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .utils.scrapper import get_items

import json


@csrf_exempt  # TODO: remove
def get_recipes(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        recipes = data.get("recipes", [])
        if not recipes:
            return JsonResponse({"message": f"Can't understand request data"}, status=422)
        response = get_items(recipes)
        return JsonResponse(response, status=200)
    else:
        return JsonResponse({"message": f"Wrong method ({request.method})"}, status=400)