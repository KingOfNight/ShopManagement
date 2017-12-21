from django.db import models

# Create your models here.
class Goods (models.Model):
    goods_name=models.CharField()
    goods_num=models.CharField()