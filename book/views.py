from django.contrib import messages
from django.shortcuts import render

from book.models import Book
from book.forms import BookForm

def create_book(request):
     if request.method == "POST":
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            data = book_form.cleaned_data
            actual_objects = Book.objects.filter(
                name=data["name"], isbn=data["isbn"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El libro {data['name']} - {data['isbn']} ya está creado",
                )
            else:
                book = Book(name=data["name"], isbn=data["isbn"], publisher=data["publisher"], author=data["author"] )
                book.save()
                messages.success(
                    request,
                    f"Libro {data['name']} - {data['isbn']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"books": Book.objects.all()},
                template_name="book/book_list.html",
            )

     book_form = BookForm(request.POST)
     context_dict = {"form": book_form}
     return render(
        request=request,
        context=context_dict,
        template_name="book/book_form.html",
    )

def books(request):
    return render(
        request=request,
        context={"books": Book.objects.all()},
        template_name="book/book_list.html",
    )

    