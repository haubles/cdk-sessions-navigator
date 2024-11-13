# models.py
from django.db import models

class Session(models.Model):
    day = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    link = models.URLField()
    sessionID = models.CharField(max_length=50)
    topic = models.CharField(max_length=200)
    area_of_interest = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    speakers = models.CharField(max_length=200)
    abstract = models.TextField()