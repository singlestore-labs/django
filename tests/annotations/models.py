from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    friends = models.ManyToManyField("self", blank=True, through="AuthorFriend")


class AuthorFriend(models.Model):
    from_author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="from_author")
    to_author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="to_author")

    class Meta:
        unique_together = (('from_author', 'to_author'),)
        db_table = "annotations_author_friend"


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    num_awards = models.IntegerField()


class Book(models.Model):
    isbn = models.CharField(max_length=9)
    name = models.CharField(max_length=255)
    pages = models.IntegerField()
    rating = models.FloatField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    authors = models.ManyToManyField("Author", through="BookAuthor")
    contact = models.ForeignKey(Author, models.CASCADE, related_name="book_contact_set")
    publisher = models.ForeignKey(Publisher, models.CASCADE)
    pubdate = models.DateField()


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('book', 'author'),)
        db_table = "annotations_book_author"


class Store(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField("Book", through="StoreBook")
    original_opening = models.DateTimeField()
    friday_night_closing = models.TimeField()
    area = models.IntegerField(null=True, db_column="surface")


class StoreBook(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('store', 'book'),)
        db_table = "annotations_store_book"


class DepartmentStore(Store):
    chain = models.CharField(max_length=255)


class Employee(models.Model):
    # The order of these fields matter, do not change. Certain backends
    # rely on field ordering to perform database conversions, and this
    # model helps to test that.
    first_name = models.CharField(max_length=20)
    manager = models.BooleanField(default=False)
    last_name = models.CharField(max_length=20)
    store = models.ForeignKey(Store, models.CASCADE)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)


class Company(models.Model):
    name = models.CharField(max_length=200)
    motto = models.CharField(max_length=200, null=True, blank=True)
    ticker_name = models.CharField(max_length=10, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)


class Ticket(models.Model):
    active_at = models.DateTimeField()
    duration = models.DurationField()
