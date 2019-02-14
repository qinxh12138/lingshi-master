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
__author__ = 'liurc'
__data__ = ' 10:25'

from apps.index.models import Shop
from haystack import indexes

class ShopIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)
    def get_model(self):
        return Shop

    def index_queryset(self, using=None):
        shop_model =  self.get_model().objects.all()
        print(shop_model)
        return shop_model
