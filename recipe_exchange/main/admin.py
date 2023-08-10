from django.contrib import admin
from .models import Profile, Category, Like, Recipe, Comment


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'gender', 'birth_date', 'user')
    list_filter = ('first_name', 'last_name', 'age', 'gender', 'birth_date', 'user')
    ordering = ('first_name', 'last_name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    ordering = ('id',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'ingredients', 'instructions', 'created_at', 'updated_at')
    list_filter = ('title', 'author', 'category', 'ingredients', 'instructions', 'created_at', 'updated_at')
    ordering = ('created_at',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'user')
    list_filter = ('recipe', 'user')
    ordering = ('user',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'author', 'text', 'created_at')
    list_filter = ('recipe', 'author', 'text', 'created_at')
    ordering = ('created_at',)
