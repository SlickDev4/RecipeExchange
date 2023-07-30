from django.db import models
from . model_managers import AppUserManager
from django.contrib.auth import models as auth_models


# accounts/models


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_FIELD = "email"

    objects = AppUserManager()

    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
        error_messages={'unique': 'Sorry, we already have a user with that email.'}
    )

    is_staff = models.BooleanField(
        default=False,
    )
