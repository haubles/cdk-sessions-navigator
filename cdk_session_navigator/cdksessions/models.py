# models.py
from django.db import models

class Session(models.Model):
    Day = models.CharField(max_length=10)
    Time = models.CharField(max_length=10)
    Location = models.CharField(max_length=100)
    Type = models.CharField(max_length=50)
    Link = models.URLField()
    SessionID = models.CharField(max_length=50)
    Topic = models.CharField(max_length=200)
    Area_of_Interest = models.CharField(max_length=100)
    Title = models.CharField(max_length=200)
    Speakers = models.CharField(max_length=200)
    Abstract = models.TextField()
