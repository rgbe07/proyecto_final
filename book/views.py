from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from book.forms import CommentForm
from book.forms import BookForm
from book.forms import EBookForm
from book.models import Comment
from book.models import Book
from book.models import EBook


class BookListView(ListView):
    model = Book
    paginate_by = 4


class BookDetailView(DetailView):
    model = Book
    template_name = "book/book_detail.html"
    fields = ["name", "isbn", "author", "publisher", "description", "image"]

    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        comments = Comment.objects.filter(book=book).order_by("-book")
        comment_form = CommentForm()
        context = {
            "book": book,
            "comments": comments,
            "comment_form": comment_form,
        }
        return render(request, self.template_name, context)


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    success_url = reverse_lazy("book:book-list")

    form_class = BookForm
    # fields = ["name", "isbn", "description", "image"]

    def form_valid(self, form):
        """Filter to avoid duplicate books"""
        data = form.cleaned_data
        form.instance.owner = self.request.user
        actual_objects = Book.objects.filter(
            name=data["name"], isbn=data["isbn"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El libro {data['name']} - {data['isbn']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Libro {data['name']} - {data['author']} creado exitosamente!",
            )
            return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ["name", "isbn", "author", "publisher", "description", "image"]

    def get_success_url(self):
        book_id = self.kwargs["pk"]
        return reverse_lazy("book:book-detail", kwargs={"pk": book_id})

    def post(self):
        pass


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy("book:book-list")


class CommentCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        comment = Comment(
            text=request.POST["comment_text"], owner=request.user, book=book
        )
        comment.save()
        return redirect(reverse("book:book-detail", kwargs={"pk": pk}))


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        book = self.object.book
        return reverse("book:book-detail", kwargs={"pk": book.id})


class EBookListView(ListView):
    model = EBook
    paginate_by = 4


class EBookCreateView(LoginRequiredMixin, CreateView):
    model = EBook
    success_url = reverse_lazy("book:ebook-list")

    form_class = EBookForm

    def form_valid(self, form):
        """Filter to avoid duplicate ebooks"""
        data = form.cleaned_data
        actual_objects = EBook.objects.filter(name=data["name"]).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El ebook {data['name']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Ebook: {data['name']}. Creado exitosamente!",
            )
            return super().form_valid(form)


class EBookDetailView(DetailView):
    model = EBook
    fields = ["name", "author", "isbn"]


class EBookUpdateView(LoginRequiredMixin, UpdateView):
    model = EBook
    fields = ["name", "author", "isbn"]

    def get_success_url(self):
        ebook_id = self.kwargs["pk"]
        return reverse_lazy("book:ebook-detail", kwargs={"pk": ebook_id})


class EBookDeleteView(LoginRequiredMixin, DeleteView):
    model = EBook
    success_url = reverse_lazy("book:ebook-list")
