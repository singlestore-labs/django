"""
One-to-one relationships

To define a one-to-one relationship, use ``OneToOneField()``.

In this example, a ``Place`` optionally can be a ``Restaurant``.
"""
from django.db import models

from django_singlestore.schema import ModelStorageManager


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name


class Restaurant(models.Model):
    place = models.OneToOneField(Place, models.CASCADE, primary_key=True)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name


class Bar(models.Model):
    place = models.OneToOneField(Place, models.CASCADE, primary_key=True)
    serves_cocktails = models.BooleanField(default=True)


class UndergroundBar(models.Model):
    place = models.OneToOneField(Place, models.SET_NULL, null=True)
    serves_cocktails = models.BooleanField(default=True)

    objects = ModelStorageManager("ROWSTORE REFERENCE")


class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)


class Favorites(models.Model):
    name = models.CharField(max_length=50)
    restaurants = models.ManyToManyField("Restaurant", through="FavoritesRestaurant")


class FavoritesRestaurant(models.Model):
    favorites = models.ForeignKey(Favorites, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('favorites', 'restaurant'),)
        db_table = "one_to_one_favorites_restaurant"


class ManualPrimaryKey(models.Model):
    primary_key = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)


class RelatedModel(models.Model):
    link = models.OneToOneField(ManualPrimaryKey, models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)


class MultiModel(models.Model):
    link1 = models.OneToOneField(Place, models.CASCADE)
    link2 = models.OneToOneField(ManualPrimaryKey, models.CASCADE)
    name = models.CharField(max_length=50)
    
    objects = ModelStorageManager(table_storage_type="ROWSTORE REFERENCE")

    def __str__(self):
        return "Multimodel %s" % self.name


class Target(models.Model):
    name = models.CharField(max_length=50, primary_key=True)


class Pointer(models.Model):
    other = models.OneToOneField(Target, models.CASCADE, primary_key=True)


class Pointer2(models.Model):
    other = models.OneToOneField(Target, models.CASCADE, related_name="second_pointer", primary_key=True)


class HiddenPointer(models.Model):
    target = models.OneToOneField(Target, models.CASCADE, related_name="hidden+", primary_key=True)


class ToFieldPointer(models.Model):
    target = models.OneToOneField(
        Target, models.CASCADE, to_field="name", primary_key=True
    )


# Test related objects visibility.
class SchoolManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_public=True)


class School(models.Model):
    is_public = models.BooleanField(default=False)
    objects = SchoolManager()


class DirectorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_temp=False)


class Director(models.Model):
    is_temp = models.BooleanField(default=False)
    school = models.OneToOneField(School, models.CASCADE, primary_key=True)
    objects = DirectorManager()
