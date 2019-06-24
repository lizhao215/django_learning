#coding=UTF-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    cname = models.CharField(unique=True, max_length=255)
    class Meta:
        managed = False
        db_table = 'shop_category'
        ordering=['id']

class Goods(models.Model):
    gname = models.CharField(max_length=255)
    gdesc = models.CharField(max_length=1024, blank=True, null=True)
    gprice = models.DecimalField(max_digits=10, decimal_places=2)
    goldprice = models.DecimalField(max_digits=10, decimal_places=2)
    categoryid = models.ForeignKey(Category, models.DO_NOTHING, db_column='categoryId_id')  # Field name made lowercase.
    def img(self):
        return self.store_set.first().color.value
    def colors(self):
        stores = self.store_set.all()
        colors=[]
        for store in stores:
            color = store.color
            if color not in colors:
                colors.append(color)
        return colors
    def sizes(self):
        stores = self.store_set.all()
        sizes=[]
        for store in stores:
            raw_sizes = store.size.all()
            for size in raw_sizes:
              if size not in sizes:
                    sizes.append(size)
        return  sizes
    class Meta:
        managed = False
        db_table = 'shop_goods'
        ordering=['-id']
#
class Goodsdetails(models.Model):
    value = models.ImageField()
    goodsid = models.ForeignKey(Goods, models.DO_NOTHING, db_column='goodsId_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shop_goodsdetails'


class Color(models.Model):
    name = models.CharField(max_length=20)
    value = models.ImageField(upload_to='color')
    class Meta:
        managed = False
        db_table = 'shop_color'

class Size(models.Model):
    value = models.CharField(max_length=255)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'shop_size'

#库存表。
class Store(models.Model):
    count = models.PositiveIntegerField()
    color=models.ForeignKey(Color)
    size=models.ManyToManyField(Size)  # 多对多
    goods=models.ForeignKey(Goods)
    def __str__(self):
        return self.goods.gname.encode("UTF-8")
    def __unicode__(self):
        return  u'(%s)'%(self.goods.gname)
    class Meta:
        db_table='shop_store'

