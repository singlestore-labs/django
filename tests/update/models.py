"""
Tests for the update() queryset method that allows in-place, multi-object
updates.
"""

from django.db import models


class DataPoint(models.Model):
    name = models.CharField(max_length=20)
    value = models.CharField(max_length=20)
    another_value = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)


class RelatedPoint(models.Model):
    name = models.CharField(max_length=20)
    data = models.ForeignKey(DataPoint, models.CASCADE)


class A(models.Model):
    x = models.IntegerField(default=10)


class B(models.Model):
    a = models.ForeignKey(A, models.CASCADE)
    y = models.IntegerField(default=10)


class C(models.Model):
    y = models.IntegerField(default=10)


class D(C):
    a = models.ForeignKey(A, models.CASCADE)


class Foo(models.Model):
    target = models.CharField(max_length=10, primary_key=True)


class Bar(models.Model):
    foo = models.ForeignKey(Foo, models.CASCADE, to_field="target")
    m2m_foo = models.ManyToManyField("Foo", related_name="m2m_foo", through="Bar_m2m_foo")
    x = models.IntegerField(default=0)


class Bar_m2m_foo(models.Model):
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)
    foo = models.ForeignKey(Foo, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('bar', 'foo'),)
        db_table = "update_bar_m2m_foo"

class UniqueNumber(models.Model):
    number = models.IntegerField(primary_key=True)


class UniqueNumberChild(UniqueNumber):
    pass
