from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from apps.index.models import Shop, SubCate


@csrf_exempt
def search(request):
    q = request.GET.get('keywords')
    if q:
        shops = Shop.objects.filter(name__icontains=q)
        if shops:
            for shop in shops:
                shop.img = shop.shopimage_set.values_list('img_url', flat=True).first()
            return render(request, 'page_search.html', {'shops': shops})
        else:
            return render(request, 'page_search.html')
    else:
        return render(request, 'page_search.html')


def search_sub(request):
    sub_cate_id = request.GET.get('keyword')
    if sub_cate_id:
        sub_cate = SubCate.objects.filter(sub_cate_id=sub_cate_id).first()
        shops = sub_cate.shop_set.all()
        if shops:
            for shop in shops:
                shop.img = shop.shopimage_set.values_list('img_url', flat=True).first()
            return render(request, 'page_search.html', {'shops': shops})
        else:
            return render(request, 'page_search.html')
    else:
        return render(request, 'page_search.html')
