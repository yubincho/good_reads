from django.urls import path

from .views import BookList, BookDetail, search

from . import views

app_name = "books"

urlpatterns = [
    path("", BookList.as_view(), name="list"),
    path("search/", views.search, name="search"),
    path("<int:pk>/", BookDetail.as_view(), name="detail"),
    path("<int:pk>/new_review/", views.review_create, name="review-create"),
]
