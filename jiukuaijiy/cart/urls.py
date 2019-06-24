from  django.conf.urls import url
from cart import views
urlpatterns=[
    url(r'^$',views.CartView.as_view()),
    url(r'^cart.html/$',views.CartListView.as_view())
]