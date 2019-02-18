# -*- coding: utf-8 -*-  
# __author__:ZHANGJIN
# __time__:2019/1/17 20:30
from django.conf.urls import url

from apps.user_account import views

urlpatterns = [
    url('login/', views.login_view, name='login'),
    url('register/', views.register_view, name='register'),
    url('logout/', views.logout_view, name='logout'),
    url('active/', views.active_account, name='active'),
    url('update_user/', views.update_view, name='update_user'),
    url('address/', views.add_address_views, name='address'),
    url('safety/', views.safety_view, name='safety'),
    url('up_pwd/', views.update_password, name='up_pwd'),
]
