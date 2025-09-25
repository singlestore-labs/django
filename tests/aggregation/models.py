from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    friends = models.ManyToManyField("self", blank=True, through="AuthorFriend")
    rating = models.FloatField(null=True)

    def __str__(self):
        return self.name


class AuthorFriend(models.Model):
    from_author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="from_author")
    to_author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="to_author")

    class Meta:
        unique_together = (('from_author', 'to_author'),)
        db_table = "aggregation_author_friend"


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    num_awards = models.IntegerField()
    duration = models.DurationField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    isbn = models.CharField(max_length=9)
    name = models.CharField(max_length=255)
    pages = models.IntegerField()
    rating = models.FloatField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    authors = models.ManyToManyField(Author, through="BookAuthor")
    contact = models.ForeignKey(Author, models.CASCADE, related_name="book_contact_set")
    publisher = models.ForeignKey(Publisher, models.CASCADE)
    pubdate = models.DateField()

    def __str__(self):
        return self.name


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('book', 'author'),)
        db_table = "aggregation_book_author"


class Store(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField("Book", through="StoreBook")
    original_opening = models.DateTimeField()
    friday_night_closing = models.TimeField()

    def __str__(self):
        return self.name


class StoreBook(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('store', 'book'),)
        db_table = "aggregation_store_book"
