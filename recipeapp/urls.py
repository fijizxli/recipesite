from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

app_name = "recipeapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("search/", views.search, name="search"),
    path("recipe/<int:r_id>/", views.recipe_detail_view, name="recipe_detail_view"),
    path("addrecipe/", views.recipe_create_view, name="recipe_create_view"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
