# -*- coding: utf-8 -*-  
# __author__:ZHANGJIN
# __time__:2019/1/17 20:30
from django.conf.urls import url

from apps.order import views

urlpatterns = [
    url('confirm/', views.confirm, name='confirm'),
    url('order_list/', views.order_list, name='order_list'),
    url('pay_shop/', views.pay_shop, name='pay_shop'),
    url(r'notify/', views.pay, name='notify'),
    url(r'pay_down/', views.pay_down, name='pay_down'),
    url(r'order_check/', views.order_check, name='order_check'),
]
