from django import forms

class BookForm(forms.Form):
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
                "required": "True",
            }
        ),
    )

class EBookForm(forms.Form):
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


class SectionForm(forms.Form):
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
    