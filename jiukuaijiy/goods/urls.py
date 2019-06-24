#coding=UTF-8
from  django.conf.urls import url
from goods import views
urlpatterns=[
url(r'^$',views.GoodsListView.as_view()),
url(r'^goodsdetails/$',views.GoodsDetailsView.as_view())
]
#index_view  ---->   index_view(request)
#views.GoodsListView.as_view()  ---> views.GoodsListView.as_view()(request)
