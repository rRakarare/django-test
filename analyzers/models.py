from django.db import models

class Analyzer(models.Model):
    brand = models.CharField(max_length=50)
    brand_logo = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    width = models.FloatField(default=0)
    depth = models.FloatField(default=0)
    height = models.FloatField(default=0)

