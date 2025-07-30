"""
Testing signals before/after saving and deleting.
"""
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Car(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)


class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=20)
    authors = models.ManyToManyField("Author", through="BookAuthor")

    def __str__(self):
        return self.name


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('book', 'author'),)
        db_table = "signals_book_author"


class Page(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
