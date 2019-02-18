import datetime
import json
import random

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import F
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from apps.user_account.context_processors import shop_count
from apps.index.models import *
from group import settings

@login_required
def list(reqeust):
    if reqeust.user.id:
        car_list = ShopCar.objects.filter(user_id=reqeust.user.id, is_delete=0)
        for car in car_list:
            car.shop = car.shop_id
            car.img = ShopImage.objects.filter(shop_id=car.shop_id).first()
        return render(reqeust, 'cate_user.html', {'car_list': car_list})
    else:
        return HttpResponse('请先登录')


@csrf_exempt
def add_car(request):
    # 判断是否是ajax请求
    if request.is_ajax():
        # 判断用户是否登录
        if request.user.is_authenticated:
            try:
                '''
              参数：商品的数量，商品id
              当商品已经存在用户的购物车的时候，更新数量，当不存在的时候创建该记录
              '''
                number = request.POST.get("number")
                shop_id = request.POST.get('shop_id')
                if number and shop_id:
                    car = ShopCar.objects.filter(shop_id=shop_id, user_id=request.user.id, is_delete=0)
                    if car.exists():
                        car.update(shop_number=F('shop_number') + number)
                    else:
                        car = ShopCar(shop_number=number, shop_id_id=shop_id, user_id_id=request.user.id)
                        car.save()
                data = shop_count(request)
                data['status'] = 200
                data['msg'] = 'success'
                return JsonResponse(data=data)
            except Exception as e:
                # 表示添加购物车失败
                return JsonResponse(data={'status': 404, 'msg': 'error'})
                # url = 'user_account/login/?next=%s' % request.path
                # return JsonResponse(data={'status': 302, 'msg': 'success', 'url': url})

        else:
            # 没有登录返回登录页面
            url = '/user_account/login/?next=/detail/detail/?sid=%s' % settings.SID
            return JsonResponse(data={'status': 302, 'msg': 'success', 'url': url})
    elif request.method == 'GET':
        return redirect(f'/{request.path}')


@csrf_exempt
def update_num(request):
    try:
        ac = request.POST.get('ac')
        car_id = request.POST.get('car_id')
        if ac == '1':
            count = ShopCar.objects.filter(car_id=car_id, is_delete=0).update(shop_number=F('shop_number') + 1)
            car = ShopCar.objects.filter(car_id=car_id).first()
            number = car.shop_number
            shop_id = car.shop_id.shop_id
            shop = Shop.objects.filter(shop_id=shop_id).first()
            price = shop.promote_price
            sum_price = number * price
            return JsonResponse({'status': 200, 'msg': 'success', 'sum_price': sum_price})
        else:
            count = ShopCar.objects.filter(car_id=car_id, is_delete=0).update(shop_number=F('shop_number') - 1)
            car = ShopCar.objects.filter(car_id=car_id).first()
            number = car.shop_number
            shop_id = car.shop_id.shop_id
            shop = Shop.objects.filter(shop_id=shop_id).first()
            price = shop.promote_price
            sum_price = number * price
            return JsonResponse({'status': 200, 'msg': 'success', 'sum_price': sum_price})
    except Exception as e:
        return JsonResponse({'status': 404, 'msg': 'error'})


def delete(request):
    if request.method == 'POST':
        shop_id = request.POST.get('shop_id')
        if shop_id:
            shop = ShopCar.objects.filter(shop_id=shop_id)
            shop.update(is_delete=1)
        return JsonResponse({'status': 200, 'msg': 'success'})
    else:
        return JsonResponse({'status': 404, 'msg': 'error'})
