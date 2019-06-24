# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from  view.views import BaseView
from  utils.pageutils import MuitlObjectReturned
from goods.models import *
class GoodsListView(BaseView,MuitlObjectReturned):
    # 所有不变的东西，都放到了类的成员当中
    template_name = 'index.html'
    objects_name = 'goods'
    category_objects = Category.objects.all()

    def prepare(self,request):
        category_id = int(request.GET.get('category',Category.objects.first().id))
        self.objects=Category.objects.get(id =category_id ).goods_set.all()
        self.category_id = category_id
    def get_extra_context(self, request):
        page_num = request.GET.get('page',1)
        context = {'category_id':self.category_id,'categorys':self.category_objects}
        context.update(self.get_objects(page_num))
        return  context

class GoodsDetailsView(BaseView):
    template_name = 'details.html'

    def handle_request_cookie(self,request):
        #获得cookie,
        # 获得cookie
        self.historys = eval(request.COOKIES.get('historys','[]'))
        pass
    def handle_response_cookie(self,response):
        # 填写用户浏览商品[id,id,id,]
        if self.goodsId not  in self.historys:
            self.historys.append(self.goodsId)
        response.set_cookie('historys',str(self.historys))
    def get_extra_context(self, request):
        goodsId = int(request.GET.get('goodsid'))
        self.goodsId = goodsId
        good = Goods.objects.get(id = goodsId)
        recomand_goods=[]
        for id in self.historys:
            recomand_goods.append(Goods.objects.get(id = id))
        return {'good':good,'goods_details':good.goodsdetails_set.all(),'recomand_goods':recomand_goods[:4]}
