from django.urls import path

from .views import list_home, add_list, remove_list

from . import views

app_name = "lists"

urlpatterns = [
    path("", views.list_home, name="list-home"),
    path("add/<int:book_id>", views.add_list, name="add-list"),
    path("remove/<int:book_id>", views.remove_list, name="remove-list"),
]
