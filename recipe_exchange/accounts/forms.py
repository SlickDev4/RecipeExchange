from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from django import forms
from recipe_exchange.main.models import Profile

# accounts/forms

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    consent = forms.BooleanField()

    first_name = forms.CharField(
        max_length=30,
        required=False,
    )

    last_name = forms.CharField(
        max_length=30,
        required=False,
    )

    password2 = forms.CharField(
        label=_("Repeat Password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.HiddenInput()
        self.fields['last_name'].widget = forms.HiddenInput()

    def save(self, commit=True):
        user = super().save(commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            user=user,
        )

        if commit:
            profile.save()

        return user

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'password1', 'password2', 'consent')


class CustomAuthenticationForm(auth_forms.AuthenticationForm):
    username = auth_forms.UsernameField(widget=forms.TextInput())
    error_messages = {
        "invalid_login": _(
            "Wrong email or password."
        ),
    }
