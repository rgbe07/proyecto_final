from django.contrib import admin

from book.models import Book, Section, EBook

admin.site.register(Book)
admin.site.register(Section)
admin.site.register(EBook)
