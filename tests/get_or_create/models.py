from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100, primary_key=True)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()
    defaults = models.TextField()
    create_defaults = models.TextField()


class DefaultPerson(models.Model):
    first_name = models.CharField(max_length=100, default="Anonymous")


class ManualPrimaryKeyTest(models.Model):
    id = models.IntegerField(primary_key=True)
    data = models.CharField(max_length=100)


class Profile(models.Model):
    person = models.ForeignKey(Person, models.CASCADE, primary_key=True)


class Tag(models.Model):
    text = models.CharField(max_length=255, primary_key=True)


class Thing(models.Model):
    name = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, through="ThingTag")

    @property
    def capitalized_name_property(self):
        return self.name

    @capitalized_name_property.setter
    def capitalized_name_property(self, val):
        self.name = val.capitalize()

    @property
    def name_in_all_caps(self):
        return self.name.upper()


class ThingTag(models.Model):
    thing = models.ForeignKey(Thing, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('thing', 'tag'),)
        db_table = "get_or_create_thing_tag"


class Publisher(models.Model):
    name = models.CharField(max_length=100)


class Author(models.Model):
    name = models.CharField(max_length=100)


class Journalist(Author):
    specialty = models.CharField(max_length=100)


class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, related_name="books", through="BookAuthor")
    publisher = models.ForeignKey(
        Publisher,
        models.CASCADE,
        related_name="books",
        db_column="publisher_id_column",
    )
    updated = models.DateTimeField(auto_now=True)


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('book', 'author'),)
        db_table = "get_or_create_book_author"
