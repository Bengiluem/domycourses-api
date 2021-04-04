from django.urls import path
from . import views


urlpatterns = [
    path('recipes/', views.recipes, name="recipes")
]
