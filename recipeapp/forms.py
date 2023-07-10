from django import forms

from .models import Recipe

# from PIL import Image


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "picture",
            "preparation_time",
            "cooking_time",
            "ingredients",
            "directions",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "title"}),
            "picture": forms.FileInput(),
            "preparation_time": forms.TextInput(
                attrs={"placeholder": "00:30:00"},
            ),
            "cooking_time": forms.TextInput(attrs={"placeholder": "02:00:00"}),
            "ingredients": forms.Textarea(
                attrs={"placeholder": "ingredients...", "rows": 4, "cols": 20},
            ),
            "directions": forms.Textarea(
                attrs={"placeholder": "directions...", "rows": 4, "cols": 20}
            ),
        }


class SearchRecipeForm(forms.ModelForm):
    q = forms.CharField(label="Search", max_length=30)
