from django import forms
from .models import Recipe, Category


class RecipeCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None)

    class Meta:
        model = Recipe
        fields = ['title', 'photo', 'category', 'ingredients', 'instructions']
