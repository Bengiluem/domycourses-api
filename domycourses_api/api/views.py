from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .utils.scrapper import get_items


@csrf_exempt  # TODO: remove
def recipes(request):
    if request.method == "POST":
        response = get_items(request.POST.get("recipes", []))
        return JsonResponse(response, status=200)
    else:
        return JsonResponse({"message": f"Wrong method ({request.method})"}, 400)
