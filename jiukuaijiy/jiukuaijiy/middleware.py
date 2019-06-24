#coding=utf-8
from  django.http.response import HttpResponseRedirect
from jiukuaijiy import  settings
from  django.http.request import HttpRequest
class UserAuth(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self, request,*args, **kwargs):
        import  re
        if request.path in  settings.AUTH:
            user = request.session.get('user', '')
            if not user:
                # 不满足条件重定向的
                return  HttpResponseRedirect('/user/login')
        # 下面是正常访问的
        return self.get_response(request)
