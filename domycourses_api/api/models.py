from django.db import models


class Recipe(models.Model):
    url = models.CharField(max_length=100, default="", primary_key=True)
    content = models.JSONField()

    def __str__(self):
        return str.format("{url} <-> {name}", url=self.url, name=self.content)
