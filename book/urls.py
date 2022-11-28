from django.urls import path

from book import views

app_name = "book"
urlpatterns = [
#    path("books", view=views.books, name = "book-list"),
#    path("book/add", view=views.create_book, name = "book-add"),
#    path("sections", view=views.sections, name = "section-list"),
#    path("section/add", view=views.create_section, name = "section-add"),
#    path("ebooks", view=views.ebooks, name = "ebook-list"),
#    path("ebook/add", view=views.create_ebook, name = "ebook-add"),


    path("books/", views.BookListView.as_view(), name="book-list"),
    path("book/add/", views.BookCreateView.as_view(), name="book-add"),
    path("book/<int:pk>/detail/", views.BookDetailView.as_view(), name="book-detail"),
    path("book/<int:pk>/update/", views.BookUpdateView.as_view(), name="book-update"),
    path("book/<int:pk>/delete/", views.BookDeleteView.as_view(), name="book-delete"),
    path("comment/<int:pk>/add/", views.CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),

    path("sections/", views.BookListView.as_view(), name="section-list"),
    path("section/add/", views.BookCreateView.as_view(), name="section-add"),



    path("ebooks", views.EBookListView.as_view(), name="ebook-list"),
    path("ebook/add/", views.EBookCreateView.as_view(), name="ebook-add"),
#    path("ebook/<int:pk>/detail/", views.EBookDetailView.as_view(), name="ebook-detail"),
#    path("ebook/<int:pk>/update/", views.EBookUpdateView.as_view(), name="ebook-update"),
#    path("ebook/<int:pk>/delete/", views.EBookDeleteView.as_view(), name="ebook-delete"),
]    