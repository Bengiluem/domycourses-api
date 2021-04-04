from django.http import JsonResponse


def index(request):
    response = {
        "hello": "world"
    }
    return JsonResponse(response, status=200)
