# ━━━━━━神兽出没━━━━━━ 
#　　　 ┏┓　　　┏┓ 
# 　　┏┛┻━━━┛┻┓ 
# 　　┃　　　　　　　┃ 
# 　　┃　　　━　　　┃ 
# 　　┃　┳┛　┗┳　┃ 
# 　　┃　　　　　　　┃ 
# 　　┃　　　┻　　　┃ 
# 　　┃　　　　　　　┃ 
# 　　┗━┓　　　┏━┛Code is far away from bug with the animal protecting 
# 　　　　┃　　　┃    神兽保佑,代码无bug 
# 　　　　┃　　　┃ 
# 　　　　┃　　　┗━━━┓ 
# 　　　　┃　　　　　　　┣┓ 
# 　　　　┃　　　　　　　┏┛ 
# 　　　　┗┓┓┏━┳┓┏┛ 
# 　　　　　┃┫┫　┃┫┫ 
# 　　　　　┗┻┛　┗┻┛ 
# ━━━━━━神兽出没━━━━━━

#-*- coding:utf_8 -*-
from django.shortcuts import render
from haystack.views import SearchView

__author__ = 'liurc'
__data__ = ' 20:23'


from .models import *

class MySeachView(SearchView):
    def create_response(self):
        context = self.get_context()
        shops = context['page']
        for shop in shops:
            shop.object.img_url =ShopImage.objects.filter(shop_id=shop.object.shop_id).values_list('img_url')[0][0]
            print(shop.object.img_url)
        context['page'] = shops

        return render(self.request, self.template, context)

