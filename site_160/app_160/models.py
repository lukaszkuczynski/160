from django.db import models


class SummaryModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    text = models.CharField(max_length=160)
    tags = models.CharField(max_length=100)

