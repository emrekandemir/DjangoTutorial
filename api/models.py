from django.db import models
from django.utils import timezone


class kategori(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateField(default=timezone.now)