from django import forms
from .models import Recipe, Category, Comment


class RecipeCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None)

    class Meta:
        model = Recipe
        fields = ['title', 'photo', 'category', 'ingredients', 'instructions']


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['placeholder'] = "Write your comment here..."
