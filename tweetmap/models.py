from django.db import models

# Create your models here.
class Tweet(models.Model):
  text = models.CharField(max_length=140)
  location = models.CharField(max_length=140)
  tweet_id = models.BigIntegerField() 
  timestamp = models.IntegerField()
  lat = models.IntegerField(null=True)
  lng = models.IntegerField(null=True)
