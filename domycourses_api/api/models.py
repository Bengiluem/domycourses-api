from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=50, primary_key=True)


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(Ingredient)
