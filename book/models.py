from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    publisher = models.CharField(max_length=20)
    isbn = models.IntegerField()

    def __str__(self):
        return f"{self.name} | {self.author} | {self.publisher} | {self.isbn}"

class Section(models.Model):
    name = models.CharField(max_length=40)
    clasification = models.IntegerField()

    def __str__(self):
        return f"{self.name} | {self.clasification}"

class EBook(models.Model):
    name = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    publisher = models.CharField(max_length=20)
    isbn = models.IntegerField()

    def __str__(self):
        return f"{self.name} | {self.author} | {self.publisher} | {self.isbn}"
