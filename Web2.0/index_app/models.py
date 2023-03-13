from django.db import models


# Create your models here.
class ZhiXiao(models.Model):
    year = models.CharField(max_length=32)
    beifen = models.CharField(max_length=32)
    guangfen = models.CharField(max_length=32)
    shangfen = models.CharField(max_length=32)
    shenfen = models.CharField(max_length=32)
    sufen = models.CharField(max_length=32)
    tianfen = models.CharField(max_length=32)
    one = models.CharField(max_length=32)
    two = models.CharField(max_length=32)


class CiYun(models.Model):
    data = models.TextField()
    one = models.CharField(max_length=32)
    two = models.CharField(max_length=32)


class Company(models.Model):
    name = models.TextField()
    reg_money = models.CharField(max_length=60)
    manage = models.CharField(max_length=60)
    brand = models.CharField(max_length=60)
    recruit = models.CharField(max_length=60)
    one = models.CharField(max_length=32)
    two = models.CharField(max_length=32)
