#coding=utf-8
from utils.alipay import AliPay
from testalipay.settings import BASE_DIR
import os
alipay = AliPay(
    appid='2016073100136733',
    app_private_key_path=os.path.join(BASE_DIR, 'keys/app_private_2048.txt'),
    alipay_public_key_path=os.path.join(BASE_DIR, 'keys/alipay_public_2048'),
    return_url='http://www.bjsxt.com', #
    app_notify_url='http://www.bjsxt.com/asd/adsasd/'
)
# 获得排序，加签的请求参数
data = alipay.direct_pay( subject='商城支付', out_trade_no='20123213', total_amount=10)

print  'https://openapi.alipaydev.com/gateway.do?'+data
