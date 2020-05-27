from django.urls import path
from . import views

# from .views import RegisterView, LoginView

app_name = "users"

urlpatterns = [
    path("profile/", views.profilepage),
    path("disable/", views.disable_request_user, name="disable-request"),
    path("delete/", views.disable_user, name="disable-user"),
]
