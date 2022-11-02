from django.contrib import messages
from django.shortcuts import render

from book.models import Book, Section, EBook
from book.forms import BookForm, SectionForm, EBookForm
 

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

def create_ebook(request):
     if request.method == "POST":
        ebook_form = EBookForm(request.POST)
        if  ebook_form.is_valid():
            data = ebook_form.cleaned_data
            actual_objects = EBook.objects.filter(
                name=data["name"], isbn=data["isbn"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El libro {data['name']} - {data['isbn']} ya está creado",
                )
            else:
                ebook = EBook(name=data["name"], isbn=data["isbn"], publisher=data["publisher"], author=data["author"] )
                ebook.save()
                messages.success(
                    request,
                    f"Libro {data['name']} - {data['isbn']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"ebooks": EBook.objects.all()},
                template_name="book/ebook_list.html",
            )

     ebook_form = EBookForm(request.POST)
     context_dict = {"form": ebook_form}
     return render(
        request=request,
        context=context_dict,
        template_name="book/ebook_form.html",
    )

def ebooks(request):
    return render(
        request=request,
        context={"ebooks": EBook.objects.all()},
        template_name="book/ebook_list.html",
    )
    
def create_section(request):
     if request.method == "POST":
        section_form = SectionForm(request.POST)
        if section_form.is_valid():
            data = section_form.cleaned_data
            actual_objects = Section.objects.filter(
                name=data["name"], clasification=data["clasification"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"La sección {data['name']} - {data['clasification']} ya está creado",
                )
            else:
                section = Section(name=data["name"], clasification=data["clasification"])
                section.save()
                messages.success(
                    request,
                    f"Sección {data['name']} - {data['clasification']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"sections": Section.objects.all()},
                template_name="book/section_list.html",
            )

     section_form = SectionForm(request.POST)
     context_dict = {"form": section_form}
     return render(
        request=request,
        context=context_dict,
        template_name="book/section_form.html",
    )

def sections(request):
    return render(
        request=request,
        context={"sections": Section.objects.all()},
        template_name="book/section_list.html",
    )
