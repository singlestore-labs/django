from django.db import models
from django.utils import timezone


class RelatedModel(models.Model):
    simple = models.ForeignKey("SimpleModel", models.CASCADE, null=True)


class SimpleModel(models.Model):
    field = models.IntegerField()
    created = models.DateTimeField(default=timezone.now)


class ManyToManyModel(models.Model):
    simples = models.ManyToManyField("SimpleModel", through="ManyToManyModelSimpleModel")


class ManyToManyModelSimpleModel(models.Model):
    manytomanymodel = models.ForeignKey(ManyToManyModel, on_delete=models.CASCADE)
    simplemodel = models.ForeignKey(SimpleModel, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('manytomanymodel', 'simplemodel'),)
        db_table = "async_manytomanymodel_simplemodel"
