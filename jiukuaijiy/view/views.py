#coding=UTF-8
from django.http.request import QueryDict
from  django.views import View
from  django.http.response import HttpResponseRedirect,HttpResponse,JsonResponse,HttpResponseBadRequest
from  django.shortcuts import  render,redirect
# 渲染,准备阶段
class BaseView(View):
    template_name = None

    def get(self,request,*args,**kwargs):
      # 准备

      if hasattr(self,'prepare') :
          getattr(self,'prepare')(request,*args,**kwargs)
      #获得cookie使用的
      if hasattr(self,'handle_request_cookie'):
          getattr(self,'handle_request_cookie')(request,*args,**kwargs)

      response = render(request, self.template_name, self.get_context(request))
      # 添加cookie使用的
      if hasattr(self,'handle_response_cookie'):
          getattr(self,'handle_response_cookie')(response,*args,**kwargs)
      return response

    def get_context(self, request):
        context = {}
        context.update(self.get_extra_context(request))
        return context

    def get_extra_context(self, request):
        return {}

# 需要处理一些业务逻辑
class BaseRedirctView(View):
    redirct_url = None
    def dispatch(self, request, *args, **kwargs):
        if hasattr(self,'handle'):
            getattr(self,'handle')(request,*args,**kwargs)
        return HttpResponseRedirect(self.redirct_url)
# 处理的都是Post请求,这个里面用不用渲染数据
# 一般来说，是不用渲染模板的，只需要返回json即可
class OperateView(View):
    form_cls = None
    def  post(self,request,*args,**kwargs):
        form = self.form_cls(request.POST.dict())
        if form.is_valid():
            handler = request.POST.get('type', '')
            if hasattr(self,handler):
                return JsonResponse(getattr(self,handler)(request,**form.cleaned_data),safe=False)
            else:
                return HttpResponseBadRequest('type没有传递')
        else:
            return JsonResponse({'errorcode':-300,'errormsg':form.errors})
