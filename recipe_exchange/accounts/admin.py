from django.contrib import admin
from .models import AppUser


# Register your models here.
@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    pass
