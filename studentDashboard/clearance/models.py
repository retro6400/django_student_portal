from django.db import models

class clear(models.Model):
    sem = models.CharField(max_length=20)
    reg = models.CharField(max_length=20)
    mid = models.CharField(max_length=20)
    fin = models.CharField(max_length=20)
