from django.urls import path
from . import views

# main/urls

urlpatterns = (
    path('', views.HomePage.as_view(), name='home'),
    path('recipes/add/', views.RecipeCreateView.as_view(), name='recipe-create'),
    path('recipes/delete/<int:pk>/', views.RecipeDeleteView.as_view(), name='recipe-delete'),
    path('recipes/edit/<int:pk>/', views.RecipeEditView.as_view(), name='recipe-edit'),
    path('recipes/like/<int:pk>/', views.RecipeLikeView.as_view(), name='recipe-like'),
    path('recipes/details/<int:pk>/', views.RecipeDetailsView.as_view(), name='recipe-details'),

    path('recipes/uploads/', views.MyRecipesView.as_view(), name='my-recipes'),
    path('recipes/liked/', views.LikedRecipesView.as_view(), name='liked-recipes'),

    path('recipes/comments/<int:pk>/', views.RecipeCommentsView.as_view(), name='recipe-comments'),
    path('recipes/comments/<int:pk>/delete/', views.DeleteCommentView.as_view(), name='delete-comment'),
    path('recipes/comments/<int:pk>/edit/', views.EditCommentView.as_view(), name='edit-comment'),

    path('profile/details/<int:pk>/', views.ProfileDetailsView.as_view(), name='profile-details'),
    path('profile/edit/<int:pk>/', views.ProfileEditView.as_view(), name='profile-edit'),
    path('profile/delete/<int:pk>/', views.ProfileDeleteView.as_view(), name='profile-delete'),
)
