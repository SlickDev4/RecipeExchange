from datetime import datetime as dt
from django import forms
from django.forms import SelectDateWidget

from .models import Recipe, Category, Comment, Profile


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


class ProfileUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(widget=SelectDateWidget(years=range(1900, dt.now().year + 1)))
    gender = forms.ChoiceField(choices=Profile.GENDER_CHOICES, widget=forms.Select())

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'age', 'gender', 'birth_date', 'photo']
