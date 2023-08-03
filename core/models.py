import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    email = models.EmailField(unique=True)

    def save(self, *args, **kwargs):
        self.username = self.email
        return super().save(*args, **kwargs)

