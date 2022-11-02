from django.urls import path

from book import views

app_name = "book"
urlpatterns = [
    path("books", view=views.books, name = "book-list"),
    path("book/add", view=views.create_book, name = "book-add"),
    path("sections", view=views.sections, name = "section-list"),
    path("section/add", view=views.create_section, name = "section-add"),
    path("ebooks", view=views.ebooks, name = "ebook-list"),
    path("ebook/add", view=views.create_ebook, name = "ebook-add"),

]