from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic

from .forms import RecipeForm
from .models import Recipe


def index(request, *args, **kwargs):
    recipes = Recipe.objects.all().order_by("-date_added")[:3]
    recipes = recipes

    context = {"recipes": recipes}
    return render(request, "recipeapp/index.html", context)


def about(request, *args, **kwargs):
    context = {
        "framework": "django",
    }

    return render(request, "recipeapp/about.html", context)


def search(request):
    searchterm = request.GET.get("q")
    if searchterm != None:
        recipes = Recipe.objects.all().filter(title__icontains=searchterm)
    else:
        recipes = Recipe.objects.all()

    context = {"recipes": recipes}
    return render(request, "recipeapp/search.html", context)


def recipe_create_view(request):
    form = RecipeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        print(form.cleaned_data)
        return redirect("/")

    context = {"form": form}
    return render(request, "recipeapp/addrecipe.html", context)


def recipe_detail_view(request, r_id):
    recipe = get_object_or_404(Recipe, id=r_id)
    context = {"recipe": recipe}
    return render(request, "recipeapp/recipe.html", context)
