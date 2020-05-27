from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        "email",
        "is_superuser",
    )


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("__str__",)


@admin.register(models.AllLogin)
class AllLoginAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
