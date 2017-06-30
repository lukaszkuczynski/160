from django.db import models


class SummaryModel(models.Model):
    author = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    text = models.CharField(max_length=160)
    tags = models.CharField(max_length=100)

