from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from ckeditor.fields import RichTextField

class Book(models.Model):
    name = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    publisher = models.CharField(max_length=20)
    isbn = models.IntegerField()
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='book', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField(
        User, through="Comment", related_name="comments_owned"
    )
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            "name",
            "author",
        )
        #ordering = ["-created_at"]
    
    
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

class Comment(models.Model):
    text = models.TextField(
        validators=[
            MinLengthValidator(10, "El comentario debe ser mayor de 10 caracteres")
        ]
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)       
