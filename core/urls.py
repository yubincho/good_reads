from django.urls import path
from books import views as book_views


app_name = "core"


urlpatterns = [
    path("", book_views.BookList.as_view(), name="home"),
]
