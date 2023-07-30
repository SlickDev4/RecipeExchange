from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
UserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f"{self.user}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.pk} - {self.name}"


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='media/', null=False, blank=False)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ingredients = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def likes_count(self):
        return Like.objects.filter(recipe=self).count()


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.email} on {self.recipe.title}'


class Like(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'Like by {self.user.email} on {self.recipe.title}'
