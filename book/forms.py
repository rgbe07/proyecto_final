from ckeditor.widgets import CKEditorWidget
from django import forms

from book.models import Book
from book.models import EBook
from book.models import Section

class BookForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre del Libro",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "book-name",
                "placeholder": "Nombre de Libro",
                "required": "True",
            }
        ),
    )

    isbn = forms.IntegerField(
        label="ISBN:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "book-isbn",
                "placeholder": "Código del Libro",
                "required": "True",
            }
        ),
    )

    author = forms.CharField(
        label="Author del Libro",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "book-author",
                "placeholder": "Author del Libro",
                "required": "True",
            }
        ),
    )

    publisher = forms.CharField(
        label="Editorial del Libro",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "book-publisher",
                "placeholder": "Editorial del Libro",
                "required": "False",
            }
        ),
    )

    description = forms.CharField(
        label="Descripción:",
        required=False,
        widget=CKEditorWidget(),
    )

    image = forms.ImageField(
        required=False,
    )

    class Meta:
        model = Book
        fields = ["name", "isbn", "author", "publisher", "description", "image"]

class EBookForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre del Libro",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "ebook-name",
                "placeholder": "Nombre de Libro",
                "required": "True",
            }
        ),
    )

    isbn = forms.IntegerField(
        label="ISBN:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "ebook-isbn",
                "placeholder": "Código del Libro",
                "required": "True",
            }
        ),
    )

    author = forms.CharField(
        label="Author del Libro",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "ebook-author",
                "placeholder": "Author del Libro",
                "required": "True",
            }
        ),
    )

    publisher = forms.CharField(
        label="Editorial del Libro",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "ebook-publisher",
                "placeholder": "Editorial del Libro",
                "required": "True",
            }
        ),
    )


class SectionForm(forms.ModelForm):
    name = forms.CharField(
        label="Seccion",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "section-name",
                "placeholder": "Nombre de la seccion",
                "required": "True",
            }
        ),
    )

    clasification = forms.CharField(
        label="Clasificación del Libro",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "section-clasification",
                "placeholder": "Clasificacion del Libro",
                "required": "True",
            }
        ),
    )
    
class CommentForm(forms.Form):
    comment_text = forms.CharField(
        label="",
        required=False,
        max_length=500,
        min_length=10,
        strip=True,
        widget=forms.Textarea(
            attrs={
                "class": "comment-text",
                "placeholder": "Ingrese su comentario...",
                "required": "True",
                "max_length": 500,
                "min_length": 10,
                "rows": 2,
                "cols": 10,
                "style":"min-width: 100%",
            }
        ),
    )    