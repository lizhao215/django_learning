#coding=utf-8
from utils.alipay import AliPay
from testalipay.settings import BASE_DIR
import os
alipay = AliPay(
    appid='2016073100136733',
    app_private_key_path=os.path.join(BASE_DIR, 'keys/app_private_2048.txt'),
    alipay_public_key_path=os.path.join(BASE_DIR, 'keys/alipay_public_2048'),
    return_url='http://127.0.0.1:8000/alipay/', #
    app_notify_url='http://www.pythoncloude.pythonanywhere.com/alipay/post'
)
from django.http.response import *
def index_view(request):
    import uuid
    pramas = alipay.direct_pay(subject='电商支付',total_amount=1000,out_trade_no=uuid.uuid4().get_hex())
    url = 'https://openapi.alipaydev.com/gateway.do?'+pramas
    # 生成线程，订单号进去，循环的查询，要么失败，要么失败，让前台界面发生跳转，web-socket,主动查询，处理同步，异步，
    return HttpResponseRedirect(url)

# 验证签名,同步通知，异步通知（支付24小时之内，不断的请求，return HttpResponse('success')）
def alipay_view(request):
     pramas = request.GET.dict()
     sign = pramas.pop('sign')
     if alipay.verify(pramas,sign):
         # 保存订单，修改订单状态
         # 查询数据库 out_trade_no uuid   trade_no和支付宝的交易号
         pramas = alipay.direct_query(pramas['out_trade_no'],pramas['trade_no'])
         url = 'https://openapi.alipaydev.com/gateway.do?' + pramas
         import requests
         response = requests.get(url)
         data = eval(response.text)['alipay_trade_query_response']
         sign = eval(response.text)['sign']

         #print alipay.verify(data,sign),'验证签名'
         if data['trade_status'] == 'TRADE_SUCCESS':
             return HttpResponse('交易成功')
         else:
             return HttpResponse('交易失败')
     else:
         return HttpResponse('支付失败')
     # 异步通知
     #return HttpResponse('success')
