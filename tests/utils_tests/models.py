from django.db import models
from django_singlestore.schema import ModelStorageManager



class Category(models.Model):
    name = models.CharField(max_length=100)


class CategoryInfo(models.Model):
    category = models.OneToOneField(Category, models.CASCADE)
    objects = ModelStorageManager("REFERENCE")
