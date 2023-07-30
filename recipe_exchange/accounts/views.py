from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import forms as auth_forms, authenticate, login
from django.contrib.auth import views as auth_views
from django.contrib.auth import mixins as auth_mixins
from django.views import generic as views
from .forms import RegisterUserForm, CustomAuthenticationForm


# accounts/views


class RegisterUserView(auth_mixins.UserPassesTestMixin, views.CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('home')


class LoginUserView(auth_mixins.UserPassesTestMixin, auth_views.LoginView):
    template_name = 'accounts/login.html'
    form_class = CustomAuthenticationForm

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('home')


class LogoutUserView(auth_views.LogoutView):
    pass
