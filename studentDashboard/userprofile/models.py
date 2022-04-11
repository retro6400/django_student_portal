from django.db import models

class userinfo(models.Model):
    username = models.CharField(max_length=20)
    sid = models.IntegerField(default=9999)
    mail = models.CharField(max_length=30)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=10)
    address = models.TextField(max_length=50)
    city = models.TextField(max_length=40)
    country = models.CharField(max_length=20)
    postal = models.IntegerField(default=00)
    about = models.TextField(max_length=200, default="about")

