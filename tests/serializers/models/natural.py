"""Models for test_natural.py"""
import uuid

from django.db import models

from django_singlestore.schema import ModelStorageManager


class NaturalKeyAnchorManager(models.Manager):
    def get_by_natural_key(self, data):
        return self.get(data=data)


class NaturalKeyAnchor(models.Model):
    data = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=100, null=True)

    objects = NaturalKeyAnchorManager()
    storage = ModelStorageManager(table_storage_type="REFERENCE")

    def natural_key(self):
        return (self.data,)


class FKDataNaturalKey(models.Model):
    data = models.ForeignKey(NaturalKeyAnchor, models.SET_NULL, null=True)


class NaturalKeyThing(models.Model):
    key = models.CharField(max_length=100, unique=True)
    other_thing = models.ForeignKey(
        "NaturalKeyThing", on_delete=models.CASCADE, null=True
    )
    other_things = models.ManyToManyField(
        "NaturalKeyThing", related_name="thing_m2m_set", through="NaturalKeyThingOtherThings"
    )

    class Manager(models.Manager):
        def get_by_natural_key(self, key):
            return self.get(key=key)

    objects = Manager()
    storage = ModelStorageManager(table_storage_type="REFERENCE")

    def natural_key(self):
        return (self.key,)

    def __str__(self):
        return self.key


class NaturalKeyThingOtherThings(models.Model):
    from_naturalkeything = models.ForeignKey(NaturalKeyThing, on_delete=models.CASCADE, related_name="from_naturalkeything")
    to_naturalkeything = models.ForeignKey(NaturalKeyThing, on_delete=models.CASCADE, related_name="to_naturalkeything")
    
    storage = ModelStorageManager(table_storage_type="ROWSTORE REFERENCE")

    class Meta:
        unique_together = (('from_naturalkeything', 'to_naturalkeything'),)
        db_table = "serializers_naturalkeything_other_things"


class NaturalPKWithDefault(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)

    class Manager(models.Manager):
        def get_by_natural_key(self, name):
            return self.get(name=name)

    objects = Manager()
    storage = ModelStorageManager(table_storage_type="REFERENCE")

    def natural_key(self):
        return (self.name,)


class FKAsPKNoNaturalKeyManager(models.Manager):
    def get_by_natural_key(self, *args, **kwargs):
        return super().get_by_natural_key(*args, **kwargs)


class FKAsPKNoNaturalKey(models.Model):
    pk_fk = models.ForeignKey(
        NaturalKeyAnchor, on_delete=models.CASCADE, primary_key=True
    )

    objects = FKAsPKNoNaturalKeyManager()

    def natural_key(self):
        raise NotImplementedError("This method was not expected to be called.")
