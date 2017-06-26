from django.db import models

from mongoengine import *

connect('160')

class SummaryModel(Document):
    author = StringField(max_length=100)
    url = StringField(max_length=100)
    text = StringField(max_length=160)
    tags = StringField(max_length=100)

