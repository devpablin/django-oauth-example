from django.db import models
from oauth2_provider.models import AbstractApplication

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    organization_id = models.CharField(max_length=15)


class Todo(models.Model):
    task = models.CharField(max_length=180)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    completed = models.BooleanField(default=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.task
