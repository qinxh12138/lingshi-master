# -*- coding: utf-8 -*-
# __author__:ZHANGJIN
# __time__:2019/1/17 20:30
from django.conf.urls import url

from apps.car import views

urlpatterns = [
    url('add/', views.add_car, name='add'),
    url('list/', views.list, name='list'),
    url('update/', views.update_num, name='update'),
    url('delete/', views.delete, name='delete')
]
