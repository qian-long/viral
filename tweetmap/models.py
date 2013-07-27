from django.db import models

# Create your models here.
class Tweet(models.Model):
  temp = models.CharField(max_length=200)
