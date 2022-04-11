from django.db import models

class dashinfo(models.Model):
    payable = models.IntegerField()
    paid = models.IntegerField()
    due = models.IntegerField()
    others = models.IntegerField()

class graphres(models.Model):
    spring22 = models.FloatField()
    fall22 = models.FloatField()

   

