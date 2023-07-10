from datetime import datetime

from django.db import models
from django.shortcuts import reverse


class Recipe(models.Model):
    title = models.CharField(max_length=80)
    picture = models.ImageField(blank=True, null=True, upload_to="photos")
    date_added = models.DateTimeField("Date added.", default=datetime.now())
    ingredients = models.TextField(max_length=300, blank=False)
    directions = models.TextField(max_length=1000, blank=False)
    cooking_time = models.DurationField()
    preparation_time = models.DurationField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse("recipe_detail_view", kwargs={"id": self.id})
        return f"/recipe/{self.id}"
