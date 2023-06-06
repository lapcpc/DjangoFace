from django.conf import settings
from django.db import models


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    done = models.BooleanField()

    def __str__(self):
        return self.task