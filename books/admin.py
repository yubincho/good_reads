from django.contrib import admin
from .models import Book, Review
from .forms import ReviewForm

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "id",
        "total_rating",
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # form = ReviewForm
    list_display = (
        "user",
        "book",
        "point",
        "point_average",
    )
