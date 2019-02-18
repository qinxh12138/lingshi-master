import datetime
import json
import random

from django.contrib.auth.decorators import login_required
from django.db import transaction

from django.http import JsonResponse, HttpResponse

from alipay import AliPay
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from group import settings
# Create your views here.


# 开始事务
from apps.index.models import ShopCar, Order, User, ShopImage, Shop


@login_required
def confirm(request):
    if request.method == 'POST':
        cars_str = request.POST.get('car')
        if cars_str:
            cars = json.loads(cars_str)
            try:
                # 开启事务
                with transaction.atomic():
                    # 生成订单
                    oid = product_order(request, cars)
                    #      做事务相关的操作
                    ShopCar.objects.all().update(status=1)
                    for car in cars:
                        ShopCar.objects.filter(car_id=car.get('car_id')).update(status=0)
                #    生成订单的操作
                return JsonResponse(data={'status': 200, 'msg': 'success', 'oid': oid})
            except Exception as e:
                transaction.rollback()
        else:
            return '404'


# 生成订单信息
def product_order(request, cars):
    # 第一步生成订单号  全站必须唯一   尽量大于8位
    user_id = request.user.id
    order_code = f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}{random.randint(100000,999999)}"
    order = Order(order_code=order_code, user_id_id=user_id)
    order.save()
    return order.oid


def add_address(request):
    if request.method == "GET":
        return render(request, 'confirm.html')
    elif request.method == "POST":
        return render(request, 'confirm.html')


@login_required
def order_list(request):
    oid = request.GET.get('oid')
    order = Order.objects.filter(oid=oid).first()
    car_list = ShopCar.objects.filter(user_id_id=request.user.id, status=0)
    for car in car_list:
        car.shop = car.shop_id
        car.img = ShopImage.objects.filter(shop_id=car.shop_id).first()
    user = User.objects.filter(id=request.user.id).first()
    address = user.address_set.all()
    return render(request, 'confirm.html', {'order': order, 'car_list': car_list, 'address': address})


@login_required
def pay_shop(request):
    if request.method == 'POST':
        cars_str = request.POST.get('car')
        if cars_str:
            cars = json.loads(cars_str)
            shop_price = 0
            order_id = 0
            for car in cars:
                car_id = car.get('car_id')
                shop_number = car.get('num')
                shopcar = ShopCar.objects.filter(car_id=car_id).first()
                shop = Shop.objects.filter(shop_id=shopcar.shop_id_id).first()
                shop_price_one = shop.promote_price
                shop_price += float(shop_price_one) * float(shop_number)
                order = Order.objects.filter(oid=car.get('oid')).first()
                order_id = order.order_code
            # print(shop_price)
            # print(order_id)
            try:
                # 支付
                settings.PAY_LIST.append((order_id, shop_price))
                Order.objects.filter(order_code=order_id).update(price=shop_price)
                #      做事务相关的操作
                return JsonResponse(data={'status': 200, 'msg': 'success'})
            except Exception as e:
                return HttpResponse('支付失败')
    else:
        return '404'


@csrf_exempt
def pay(request):
    alipay = AliPay(
        appid=settings.APP_ID,
        app_notify_url='http://127.0.0.1:8000/pay/notify/',
        app_private_key_path=settings.APP_PRIVATE_KEY_PATH,
        alipay_public_key_path=settings.ALIPAY_PUBLIC_KEY_PATH,
        sign_type='RSA2',
        debug=True
    )
    # 生成订单参数
    # 电脑网站的支付地址  https://openapi.alipaydev.com/gateway.do?order_url
    order_url = alipay.api_alipay_trade_page_pay(
        subject='91零食订单',
        out_trade_no=settings.PAY_LIST[-1][0],
        total_amount=str(settings.PAY_LIST[-1][1]),
        return_url='http://127.0.0.1:8000/pay/pay_down/',  # 支付成功后前端跳转的网址
        notify_url='后台接收支付宝支付相关信息的接口 post请求'
    )
    pay_url = settings.ALT_PAY_DEV_URL + order_url
    uid = request.user.id
    order = Order.objects.filter(user_id_id=uid, order_code=settings.PAY_LIST[-1][0]).first()
    ShopCar.objects.filter(user_id_id=uid).update(is_status=1, o_id=order.oid, is_delete=1)
    Order.objects.filter(user_id_id=uid, order_code=settings.PAY_LIST[-1][0]).update(pay_time=datetime.datetime.now())
    return redirect(pay_url)


@csrf_exempt
def notify_callback(request):
    json_data = request.POST.get('sign')
    pass


def pay_down(request):
    uid = request.user.id
    order = Order.objects.filter(user_id_id=uid,order_code=settings.PAY_LIST[-1][0]).first()
    user = User.objects.filter(id=request.user.id).first()
    address = user.address_set.first()
    return render(request,'success.html',{'order':order,'address':address})


def order_check(request):
    uid = request.user.id
    order = Order.objects.filter(user_id_id=uid).all()
    for list in order:
        list.car_list = ShopCar.objects.filter(user_id_id=uid, o_id=list.oid)
        for car in list.car_list:
            car.shop = car.shop_id
            car.img = ShopImage.objects.filter(shop_id=car.shop_id).first()
    return render(request, 'order.html', {'order':order})