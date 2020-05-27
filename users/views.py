import os
import requests

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .models import User
from . import models

# Create your views here.


@login_required
def profilepage(request):
    return render(request, "users/profile.html")


def home(request):
    return render(request, "base.html")


@login_required
def disable_request_user(request):
    return render(request, "users/delete_user.html")


@login_required
def disable_user(request):
    pk = request.user.id
    user = User.objects.get(pk=pk)
    if request.user.is_authenticated and request.user.id == user.id:
        if request.method == "POST":
            user.delete()
            return redirect("account_logout")
    return render(request, "users:profile.html")
