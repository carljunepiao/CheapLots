from __future__ import unicode_literals
from django.db import models


# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default='Description default text')

    def __str__(self):
        return self.name
