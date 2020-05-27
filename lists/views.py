from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from books.models import Book
from .models import List

# Create your views here.


def list_home(request):
    list_obj, new_obj = List.objects.new_or_get(request)
    return render(request, "lists/list_home.html", {"list": list_obj})


@login_required
def add_list(request, book_id):

    if book_id is not None:
        try:
            book_obj = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            # print("Show message to user, book is gone?")
            return redirect("lists:list-home")
        list_obj, new_obj = List.objects.new_or_get(request)
        if book_obj in list_obj.books.all():
            messages.success(request, f"이미 목록에 있습니다.")
            return redirect(book_obj.get_absolute_url())
            # list_obj.books.remove(book_obj)
        else:
            list_obj.books.add(book_obj)

    return redirect("lists:list-home")


@login_required
def remove_list(request, book_id):
    book_obj = get_object_or_404(Book, id=book_id)
    list_obj, new_obj = List.objects.new_or_get(request)
    if book_obj in list_obj.books.all():

        if list_obj.books.count() > 1:
            list_obj.books.remove(book_obj)
            list_obj.save()
        else:
            list_obj.delete()
    return redirect("lists:list-home")
