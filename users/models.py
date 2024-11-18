from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Avoid clash with default auth.User
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_set_permissions",  # Avoid clash with default auth.User
        blank=True,
    )
