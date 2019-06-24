# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.request import QueryDict
from django.shortcuts import render

# Create your views here.
from view.views import BaseRedirctView,BaseView,OperateView

# CartView完成的功能
from utils.cartutils import *
from django import forms
class MyForm(forms.Form):
    goodsid = forms.IntegerField()
    colorid = forms.IntegerField()
    sizeid  = forms.IntegerField()
    count = forms.IntegerField(required=False)
    def clean(self):
        super(MyForm,self).clean()
        data = self.cleaned_data
        count = data['count']
        # if count<0:
        #     self.errors['count']=['商品数量不能小于0']

class CartView(BaseRedirctView):
    """添加购物项，重定向到购物车界面"""
    redirct_url = '/cart/cart.html'
    def handle(self,request,*args,**kwargs):
        request.session.modified = True
        cart_manager = SessionCartManager(request.session)
        cart_manager.add_cart_item(**request.POST.dict())
        pass


class CartListView(BaseView,OperateView):
    template_name = 'cart.html'
    form_cls = MyForm
    def get_extra_context(self, request):
        cart_manager = SessionCartManager(request.session)
        return {'cartItems':cart_manager.get_all_cart_items()}

    def add(self,request,goodsid,colorid,sizeid,*args,**kwargs):
       request.session.modified = True
       cart_manager = SessionCartManager(request.session)
       try:
           cart_manager.add_cart_item(goodsid=goodsid, colorid=colorid, sizeid=sizeid, count=1)
           return {"errorcode": 200, 'errormsg': ""}
       except Exception as e:
           return {"errorcode": -100, 'errormsg': e.message}

    def min(self, request, goodsid, colorid, sizeid, *args, **kwargs):
        request.session.modified = True
        cart_manager = SessionCartManager(request.session)
        try:
            cart_manager.add_cart_item(goodsid=goodsid, colorid=colorid, sizeid=sizeid, count=-1)
            return {"errorcode": 200, 'errormsg': ""}
        except Exception as e:
            return {"errorcode": -100, 'errormsg': e.message}

    def delete(self,request,goodsid,colorid,sizeid,*args,**kwargs):
        request.session.modified = True
        cart_manager = SessionCartManager(request.session)
        try:
            cart_manager.delete_cart_item(goodsid=goodsid,colorid=colorid,sizeid=sizeid)
            return {"errorcode": 200, 'errormsg': ""}
        except Exception as e:
            return {"errorcode": -100, 'errormsg': "删除失败"}