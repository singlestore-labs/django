from django.db import models
from django_singlestore.schema import ModelStorageManager


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    objects = ModelStorageManager("REFERENCE")


class UserStatResult(models.Model):
    results = models.CharField(max_length=50)


class UserStat(models.Model):
    user = models.OneToOneField(User, models.CASCADE, primary_key=True)
    posts = models.IntegerField()
    results = models.ForeignKey(UserStatResult, models.CASCADE)
    objects = ModelStorageManager("REFERENCE")



class StatDetails(models.Model):
    base_stats = models.OneToOneField(UserStat, models.CASCADE)
    comments = models.IntegerField()
    objects = ModelStorageManager("REFERENCE")



class AdvancedUserStat(UserStat):
    karma = models.IntegerField()


class Image(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.OneToOneField(Image, models.SET_NULL, null=True)
    objects = ModelStorageManager("REFERENCE")



class Parent1(models.Model):
    name1 = models.CharField(max_length=50)


class Parent2(models.Model):
    # Avoid having two "id" fields in the Child1 subclass
    id2 = models.AutoField(primary_key=True)
    name2 = models.CharField(max_length=50)


class Child1(Parent1, Parent2):
    value = models.IntegerField()
    objects = ModelStorageManager("REFERENCE")


class Child2(Parent1):
    parent2 = models.OneToOneField(Parent2, models.CASCADE)
    value = models.IntegerField()
    objects = ModelStorageManager("REFERENCE")



class Child3(Child2):
    value3 = models.IntegerField()


class Child4(Child1):
    value4 = models.IntegerField()


class LinkedList(models.Model):
    name = models.CharField(max_length=50)
    previous_item = models.OneToOneField(
        "self",
        models.CASCADE,
        related_name="next_item",
        blank=True,
        null=True,
    )
    objects = ModelStorageManager("REFERENCE")
