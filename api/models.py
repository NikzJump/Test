# Модели данных

from django.db import models

STATUS_CHOICES = (
    ("in stock", "в наличии"),
    ("issued", "выдана"),
)


class Book(models.Model):
    title = models.CharField(max_length=99)
    author = models.CharField(max_length=199)
    year = models.IntegerField(default=0)
    status = models.CharField(
        max_length=9,
        choices=STATUS_CHOICES,
        default="in stock",
    )
