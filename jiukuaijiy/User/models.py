# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from utils.commonutils import md
# 账号,密码(md5)
# Create your models here.
# 对称加密（用什么加密用什么解密（^））
# 非对称加密（rsa）
class User(models.Model):
    account = models.CharField(unique=True,max_length=20)
    password = models.CharField(max_length=64)
    class RegisterException(Exception):
        pass
    class LoginException(Exception):
        pass
    @staticmethod
    def register(account ,password,*args,**kwargs):
        try:
           return User.objects.create(account=account,password=password)
        except Exception as e:
            print  e.message
            raise  User.RegisterException()
    @staticmethod
    def login(account,password,time,*args,**kwargs):
        import  time as t
        current_server = t.time()*1000
        if not (int(time) >= current_server-1000*60*10 and int(time) <= current_server):
            return
        try:
            # 先通过账号获得用户
            user = User.objects.get(account=account)
            user_password = md(user.password+time)
            if user_password == password:
                return user
            else:
                return None
        except Exception as e:
            raise User.LoginException()

class Address(models.Model):
    province = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    area = models.CharField(max_length=10)
    details = models.CharField(max_length=520)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    user = models.ForeignKey(User)
    isdelete = models.BooleanField(default=False)
    # 默认收货地址
    isprimary = models.BooleanField(default=False)