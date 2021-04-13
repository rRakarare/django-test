from django.db import models

class Analyzer(models.Model):
    brand = models.CharField(max_length=50)
    brand_logo = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    width = models.FloatField()
    depth = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return f"{self.name}"

