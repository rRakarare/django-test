from django.db import models

class Analyzer(models.Model):
    name = models.CharField(max_length=50)
