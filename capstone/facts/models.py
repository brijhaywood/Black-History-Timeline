from django.db import models

# Create your models here.
class Facts(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=100, default = "")
    lat = models.FloatField()
    long = models.FloatField()

    