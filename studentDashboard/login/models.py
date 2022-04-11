from statistics import mode
from django.db import models


class logdata(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class active(models.Model):
    act = models.CharField(max_length=20)