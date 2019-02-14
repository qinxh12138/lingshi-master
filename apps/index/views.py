from django.shortcuts import render
from apps.index.models import Category, Banner, ShopImage, SubCate


# Create your views here.

def index(request):
    banners = Banner.objects.all()
    category_list = Category.objects.all()
    sub_cate_es = SubCate.objects.all()
    for cate in category_list:
        cate.sub_cate_list = cate.subcate_set.all()
    for sub_cate in sub_cate_es:
        sub_cate.shops = sub_cate.shop_set.all().values('shop_id', 'name', 'promote_price')
        for shop in sub_cate.shops:
            shop.update(img=ShopImage.objects.filter(shop_id=shop.get('shop_id')).first())
    return render(request, 'index.html', {'category_list': category_list, 'sub_cate_es': sub_cate_es})
