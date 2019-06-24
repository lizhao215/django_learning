# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from User.models import *
from  view.views import *
# Create your views here.
class RegisterView(BaseView):
    template_name = 'register.html'

class RegisterControlView(BaseRedirctView):
    redirct_url = '/user/usercenter/'

    # 完成表单的验证
    def handle(self, request, *args, **kwargs):
        user = User.register(**request.POST.dict())
        request.session['user'] = user

# 每次登陆发给服务器的密码都不一样
# md5   *加盐,(客户端加密)
#password = hex_md5(password)
# password = hex_md5(password+'时间')
# 时间
#password = md.update(password+'时间')
# 匹配
class UserCenterView(BaseView):
    template_name = 'user.html'




class LoginView(BaseView):
    template_name = 'login.html'
class LoginControl(BaseRedirctView):
    redirct_url = '/user/usercenter/'
    def handle(self,request,*args,**kwargs):
        user = User.login(**request.POST.dict())
        print  user,'用户登录成功没有'
        request.session['user']=user

from utils.commonutils import *
from django import forms
class AddressForm(forms.Form):
    provinceid = forms.IntegerField(required=False)
    cityid = forms.IntegerField(required=False)
    areaid = forms.IntegerField(required=False)
    details = forms.CharField(required=False)
    name = forms.CharField(required=False)
    phone = forms.CharField(required=False)




class AddressView(BaseView,OperateView):
    form_cls = AddressForm
    template_name = 'address.html'
    def get_extra_context(self, request):
       default_citys =  get_citys_by_id(provinces[0]['id'])
       default_areas=get_areas_by_id(default_citys[0]['id'])
       user = request.session['user']
       address = user.address_set.all()

       return {'provinces':provinces,'citys':default_citys,'areas':default_areas,'address':address}
    def get_province(self,request,provinceid,*args,**kwargs):
        data=[]
        citys  = get_citys_by_id(str(provinceid))
        data.append(citys)
        data.append(get_areas_by_id(citys[0]['id']))
        return data
    def get_citys(self,request,cityid,*args,**kwargs):
        return get_areas_by_id(str(cityid))

    def save_address(self,request,name,phone,provinceid,areaid,cityid,details):
        user = request.session['user']
        province = get_province_by_id(provinceid)
        city = get_city_by_id(provinceid,cityid)
        area = get_area_by_id(cityid,areaid)
        try:
            address = Address.objects.create(name=name,phone=phone,province=province,city=city,area=area,details=details,user=user)
            return {'errorcode':200,'errormsg':''}
        except:
            return {'errorcode':-300,'errormsg':'添加失败'}


