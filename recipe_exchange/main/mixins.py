from django.core.exceptions import PermissionDenied
from django.views import generic as views


class OnlyAuthorAccessMixin(views.View):
    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if obj.author != self.request.user:
            raise PermissionDenied
        return obj


class PopulateEditDeleteFormMixin(views.base.ContextMixin, views.View):
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        recipe = self.get_object()
        form.initial['title'] = recipe.title
        form.initial['photo'] = recipe.photo
        form.initial['category'] = recipe.category
        form.initial['ingredients'] = recipe.ingredients
        form.initial['instructions'] = recipe.instructions
        return form
