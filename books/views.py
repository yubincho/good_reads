from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

from users.models import User
from .models import Book, Review
from .forms import ReviewForm
from . import forms

# Create your views here.


class BookList(ListView):
    model = Book
    template_name = "books/book_list.html"


class BookDetail(DetailView):
    model = Book
    queryset = Book.objects.all()

    # context_object_name = "book"
    template_name = "books/book_detail.html"

    def get_object(self, *args, **kwargs):
        object = super().get_object()
        object.views_count += 1
        object.save()
        return object

    def get_context_data(self, **kwargs):
        context = super(BookDetail, self).get_context_data(**kwargs)
        context["form"] = ReviewForm()
        return context


def review_create(request, pk):
    book = get_object_or_404(Book, pk=pk)

    errors = []
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()

            if not review.content:
                errors.append("댓글을 입력해주세요.")

            return redirect(book.get_absolute_url())
    else:
        form = ReviewForm()
    return render(request, "books/book_detail.html", {"form": form})


def search(request):

    books = Book.objects.all().order_by("-id")
    # qs = Board.objects.all()
    search = request.GET.get("search")

    if not search == "" and search is not None:
        books = books.filter(title__icontains=search)

    return render(request, "books/search.html", {"books": books, "search": search})
