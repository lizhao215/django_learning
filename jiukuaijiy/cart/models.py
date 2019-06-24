# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# . 字典，属性，方法，索引  list.0
# Create your models here.
from  goods.models import *
class CartItemManager(models.Manager):
    def all(self):
        return super(CartItem,self).all().filter(isdelete=False)
class CartItem(models.Model):
    goodsid = models.IntegerField()
    colorid = models.IntegerField()
    sizeid = models.IntegerField()
    count = models.IntegerField()
    isdelete = models.BooleanField(default=False)
    objects = CartItemManager()
    def goods(self):
        return Goods.objects.get(id = self.goodsid)
    def color(self):
        return Color.objects.get(id = self.colorid)
    def size(self):
        return Size.objects.get(id = self.sizeid)
    def all_price(self):
        return self.goods().gprice*(int(self.count))


