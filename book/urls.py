from django.urls import path

from book import views

app_name = "book"
urlpatterns = [
    path("books", view=views.books, name = "book-list"),
    path("book/add", view=views.create_book, name = "book-add"),

]