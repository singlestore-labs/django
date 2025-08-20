from django.db import models

from django_singlestore.schema import ModelStorageManager


class ParentManager(models.Manager):
    def get_by_natural_key(self, parent_data):
        return self.get(parent_data=parent_data)


class Parent(models.Model):
    parent_data = models.CharField(max_length=30, unique=True)
    parent_m2m = models.ManyToManyField("Parent", through="ParentParent")

    objects = ParentManager()
    storage = ModelStorageManager(table_storage_type="ROWSTORE REFERENCE")

    def natural_key(self):
        return (self.parent_data,)


class ParentParent(models.Model):
    from_parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name="from_parent")
    to_parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name="to_parent")

    class Meta:
        unique_together = (('from_parent', 'to_parent'),)
        db_table = "serializers_parent_parent"


class Child(Parent):
    child_data = models.CharField(max_length=30, unique=True)
    storage = ModelStorageManager(table_storage_type="ROWSTORE REFERENCE")
