# -*- coding: utf-8 -*-  
# __author__:ZHANGJIN
# __time__:2019/1/17 20:30
from django.conf.urls import url

from apps.search import views

urlpatterns = [
    url('search/', views.search, name='search'),
    url('search_cate/', views.search_sub, name='search_sub')
]
