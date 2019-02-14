from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from apps.index.models import Shop, ShopImage, ShopProperty


def detail(request):
    sid = request.GET.get('sid')
    if sid:
        try:
            shops = Shop.objects.filter(shop_id=sid).values(
                'shop_id',
                'name',
                'promote_price',
                'original_price',
                'stock',
                'quantity',
            )
            if shops.exists():
                shop = shops.first()
                imgs = ShopImage.objects.filter(shop_id=shop.get('shop_id')).values('img_url')
                shop.update(imgs=imgs)
                values = ShopProperty.objects.filter(shop_id=shop.get('shop_id'))
                x = Shop.objects.filter(shop_id=sid).first()
                cate_name = x.sub_cate_id.name
                return render(request, 'shop_detail.html', {'shop': shop, 'cate_name': cate_name, 'values': values})
            else:
                return HttpResponse('错误')
        except Exception as e:
            print(e)
    else:
        return HttpResponse('404')
