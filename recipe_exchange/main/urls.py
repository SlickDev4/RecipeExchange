from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# main/urls

urlpatterns = (
    path('', views.HomePage.as_view(), name='home'),
    path('recipes/add/', views.RecipeCreateView.as_view(), name='recipe-create'),
    path('recipes/delete/<int:pk>/', views.RecipeDeleteView.as_view(), name='recipe-delete'),
    path('recipes/edit/<int:pk>/', views.RecipeEditView.as_view(), name='recipe-edit'),
    path('recipes/like/<int:pk>/', views.RecipeLikeView.as_view(), name='recipe-like'),
    path('recipes/details/<int:pk>/', views.RecipeDetailsView.as_view(), name='recipe-details')
)
