from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins
from .models import Profile, Recipe, Like
from .forms import RecipeCreateForm
from .mixins import PopulateEditDeleteFormMixin, OnlyAuthorAccessMixin


# main/views


class LandingPage(views.TemplateView):
    template_name = 'main/landing-page.html'
    login_url = 'home'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.login_url)
        else:
            return super().get(request, *args, **kwargs)


class HomePage(auth_mixins.LoginRequiredMixin, views.ListView):
    template_name = 'main/home.html'
    model = Recipe
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(user=self.request.user)
        context['profile'] = profile

        for recipe in context['recipes']:
            recipe.likes_count = Like.objects.filter(recipe=recipe).count()

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-updated_at')


class RecipeCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'main/recipe-create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        recipe = form.save(commit=False)
        recipe.author = self.request.user
        recipe.save()
        return super().form_valid(form)


class RecipeEditView(auth_mixins.LoginRequiredMixin, PopulateEditDeleteFormMixin, OnlyAuthorAccessMixin, views.UpdateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'main/recipe-edit.html'
    success_url = reverse_lazy('home')


class RecipeDeleteView(auth_mixins.LoginRequiredMixin, PopulateEditDeleteFormMixin, OnlyAuthorAccessMixin, views.DeleteView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'main/recipe-delete.html'
    success_url = reverse_lazy('home')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        for field in form.fields.values():
            field.disabled = True
        return form


class RecipeLikeView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = "main/home.html"
    model = Like
    fields = []

    def form_valid(self, form, *args, **kwargs):
        recipe_id = self.kwargs['pk']
        recipe = get_object_or_404(Recipe, id=recipe_id)

        like = form.save(commit=False)
        like.recipe = recipe
        like.user = self.request.user
        like.save()

        return HttpResponseRedirect(self.get_success_url())

    def post(self, request, *args, **kwargs):
        recipe_id = self.kwargs['pk']
        recipe = get_object_or_404(Recipe, id=recipe_id)

        liked = Like.objects.filter(user=request.user, recipe=recipe).exists()

        if liked:
            Like.objects.filter(user=request.user, recipe=recipe).delete()
        else:
            Like.objects.create(user=request.user, recipe=recipe)

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('home')
