from django.urls import path
from . import views

# accounts/urls


urlpatterns = (
    path('register/', views.RegisterUserView.as_view(), name='register-user'),
    path('login/', views.LoginUserView.as_view(), name='login-user'),
    path('logout/', views.LogoutUserView.as_view(), name='logout-user'),
)
