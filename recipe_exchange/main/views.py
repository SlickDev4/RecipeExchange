from django.db.models import Max
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins
from .models import Profile, Recipe, Like, Comment
from .forms import RecipeCreateForm, CommentCreateForm
from .mixins import PopulateEditDeleteFormMixin, OnlyAuthorAccessMixin

# main/views


class HomePage(
    views.ListView
):
    template_name = 'main/home.html'
    model = Recipe
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            profile = Profile.objects.get(user=self.request.user)
            context['profile'] = profile

        for recipe in context['recipes']:
            recipe.likes_count = Like.objects.filter(recipe=recipe).count()

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-updated_at')


class RecipeCreateView(
    auth_mixins.LoginRequiredMixin,
    views.CreateView
):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'main/recipe-create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        recipe = form.save(commit=False)
        recipe.author = self.request.user
        recipe.save()
        return super().form_valid(form)


class RecipeEditView(
    auth_mixins.LoginRequiredMixin,
    PopulateEditDeleteFormMixin,
    OnlyAuthorAccessMixin,
    views.UpdateView
):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'main/recipe-edit.html'
    success_url = reverse_lazy('home')


class RecipeDeleteView(
    auth_mixins.LoginRequiredMixin,
    PopulateEditDeleteFormMixin,
    OnlyAuthorAccessMixin,
    views.DeleteView
):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'main/recipe-delete.html'
    success_url = reverse_lazy('home')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        for field in form.fields.values():
            field.disabled = True
        return form


class RecipeLikeView(
    auth_mixins.LoginRequiredMixin,
    views.CreateView
):
    template_name = "main/recipe-details.html"
    model = Like
    fields = []

    def form_valid(self, form, *args, **kwargs):
        recipe_id = self.kwargs['pk']
        recipe = get_object_or_404(Recipe, id=recipe_id)

        like = form.save(commit=False)
        like.recipe = recipe
        like.user = self.request.user
        like.save()

        return self.custom_redirect(recipe_id)

    def post(self, request, *args, **kwargs):
        recipe_id = self.kwargs['pk']
        recipe = get_object_or_404(Recipe, id=recipe_id)

        liked = Like.objects.filter(user=request.user, recipe=recipe).exists()

        if liked:
            Like.objects.filter(user=request.user, recipe=recipe).delete()
        else:
            Like.objects.create(user=request.user, recipe=recipe)

        return self.custom_redirect(recipe_id)

    def custom_redirect(self, recipe_id):
        recipe_details_url = reverse_lazy('recipe-details', args=[recipe_id])
        return redirect(recipe_details_url)


class RecipeDetailsView(
    views.DetailView
):
    template_name = "main/recipe-details.html"
    model = Recipe
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_id = self.kwargs['pk']
        recipe = get_object_or_404(Recipe, id=recipe_id)

        if self.request.user.is_authenticated:
            liked = Like.objects.filter(user=self.request.user, recipe=recipe).exists()
            context['liked'] = liked
            context['author_or_user'] = 'True' if self.request.user == recipe.author else 'False'

        return context


class RecipeCommentsView(
    auth_mixins.LoginRequiredMixin,
    views.CreateView,
    views.ListView
):
    template_name = "main/recipe-comments.html"
    model = Comment
    form_class = CommentCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        recipe_id = self.kwargs['pk']
        recipe = get_object_or_404(Recipe, id=recipe_id)

        context['recipe'] = recipe
        context['author_or_user'] = 'True' if self.request.user == recipe.author else 'False'
        context['filtered_comments'] = Comment.objects.filter(recipe=recipe).order_by('-created_at')

        return context

    def form_valid(self, form, *args, **kwargs):
        recipe_id = self.kwargs['pk']
        recipe = get_object_or_404(Recipe, id=recipe_id)

        comment = form.save(commit=False)
        comment.recipe = recipe
        comment.author = self.request.user
        comment.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('recipe-comments', kwargs={'pk': self.kwargs['pk']})


class DeleteCommentView(
    auth_mixins.LoginRequiredMixin,
    OnlyAuthorAccessMixin,
    views.DeleteView
):
    template_name = 'main/delete-comment.html'
    model = Comment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_id'] = self.kwargs['pk']
        context['recipe_id'] = self.get_object().recipe.pk
        return context

    def get_success_url(self):
        recipe_pk = self.get_object().recipe.pk
        return reverse_lazy('recipe-comments', args=[recipe_pk])


class EditCommentView(
    auth_mixins.LoginRequiredMixin,
    OnlyAuthorAccessMixin,
    views.UpdateView
):
    model = Comment
    form_class = CommentCreateForm
    template_name = 'main/edit-comment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_id'] = self.get_object().recipe.pk
        return context

    def get_success_url(self):
        recipe_pk = self.get_object().recipe.pk
        return reverse_lazy('recipe-comments', args=[recipe_pk])
