from django.contrib import admin
from .models import List

# Register your models here.


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "__str__",
    )
    filter_horizontal = ("books",)

