from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django_singlestore.schema import ModelStorageManager


class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    custom_objects = BaseUserManager()

    USERNAME_FIELD = "email"

    objects = ModelStorageManager("REFERENCE")

    class Meta:
        app_label = "test_client_regress"
