from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=255)
    date = models.CharField(max_length=4)
