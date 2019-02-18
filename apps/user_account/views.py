import re
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.db import transaction
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from itsdangerous import URLSafeSerializer
from apps.index.models import User, Address
from group import settings
from django.template import loader
from django.core.cache import cache


# 登录
@csrf_exempt
def login_view(request):
    if request.method == 'GET':
        redirect_url = request.GET.get('next')
        return render(request, 'login.html', {'next': redirect_url})
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        redirect_url = request.POST.get('next')
        user = authenticate(request, username=username, password=password) or authenticate(request, email=username,
                                                                                           password=password) or authenticate(
            request, phone=username, password=password)
        if user:
            # 判断用户是否激活
            if user.is_active:
                # 记住用户状态
                login(request, user)
                if redirect_url:
                    # 返回之前的页面
                    return redirect(redirect_url)
                else:
                    # 返回首页
                    return redirect('/')
            else:
                # 表示用户被禁用
                return render(request, 'login.html', {'msg': '账户已经被锁定，请于管理员联系'})
        else:
            # 登录失败
            return render(request, 'login.html', {'msg': '账号或密码错误'})


# 注册
@csrf_exempt
def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        user = User.objects.filter(username=username)
        password = request.POST.get('password')
        verity_password = request.POST.get('passwordRepeat')
        email = request.POST.get('email')
        if not re.match('(^[a-zA-Z0-9_-]{4,16}$)', username):
            return render(request, 'register.html', {'msg': '用户名不符合规范'})
        # 查询用户是否存在
        if user.exists():
            return render(request, 'register.html', {'msg': '用户名已存在'})
        # 判断两次密码是否一致
        if password != verity_password:
            return render(request, 'register.html', {'msg': '两次密码不一致'})
        # 正则验证密码是否符合规范
        if not re.match('(^.*(?=.{6,})(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*? ]).*$)', password):
            return render(request, 'register.html', {'msg': '密码不符合规范'})
        # 正则验证邮箱是否符合规范
        if not re.match('(^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$)', email):
            return render(request, 'register.html', {'msg': '邮箱不符合规范'})
        # 用户注册成功
        try:
            with transaction.atomic():
                user = User.objects.create_user(username=username, password=password, email=email, is_active=0)
                if user:
                    auth_s = URLSafeSerializer(settings.SECRET_KEY, 'auth')
                    token = auth_s.dumps({'uid': user.id})
                    cache.set(token, user.id, timeout=10 * 60)
                    active_url = f'http://127.0.0.1:8000/user_account/active/?token={token}'
                    content = loader.render_to_string('mail.html',
                                                      request=request,
                                                      context={'username': username, 'active_url': active_url})
                    send_active_mail(subject='零食在线激活邮件', content=content, to=[email])
                    return redirect('/')
        except Exception as e:
            return render(request, 'register.html', {'msg': '注册失败'})


# 注销
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


# 更新
@login_required
@csrf_exempt
def update_view(request):
    if request.method == 'GET':
        return render(request, 'personal.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        new_phone = request.POST.get('new_phone')
        new_email = request.POST.get('new_email')
        user = request.user
        user.username = username
        user.first_name = first_name
        user.phone = new_phone
        user.email = new_email
        user.save()
        return render(request, 'personal.html')


@login_required
@csrf_exempt
def add_address_views(request):
    if request.method == 'GET':
        try:
            address_list = Address.objects.filter(user_id=request.user.id)
            return render(request, 'address.html', {'address_list': address_list})
        except:
            return render(request, 'address.html')

    if request.method == 'POST':
        receiver = request.POST.get('receiver')
        phone = request.POST.get('phone')
        province = request.POST.get('province')
        city = request.POST.get('city')
        area = request.POST.get('area')
        detail_address = request.POST.get('detail_address')
        address = Address(receiver=receiver, phone=phone, province=province, city=city, area=area,
                          detail_address=detail_address, user_id=request.user)
        address.save()
        address_list = Address.objects.filter(user_id=request.user.id)
        return render(request, 'address.html', {'address_list': address_list})


def active_account(request):
    # uid = request.GET.get('id')
    token = request.GET.get('token')
    uid = cache.get(token)
    if uid:
        User.objects.filter(id=uid).update(is_active=1)
        return redirect('/')
    else:
        # 激活已经失效
        # 输入邮箱或者用户名     通过用户或者邮箱查询user对象
        return redirect('/')


# 发送邮件
def send_active_mail(subject='', content=None, to=None):
    send_mail(subject=subject,
              message='',
              html_message=content,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=to
              )


@login_required
@csrf_exempt
def safety_view(request):
    user = request.user
    if user:
        return render(request, 'safety.html', {'user': user})
    else:
        return render(request, 'login.html')


@login_required
@csrf_exempt
def update_password(request):
    if request.method == 'GET':
        return render(request, 'up_pwd.html')
    if request.method == 'POST':
        user = request.user
        if user:
            password = request.POST.get("password")
            new_password = request.POST.get("newpassword")
            pwd = user.check_password(password)
            if pwd:
                user.password = make_password(new_password)
                user.save()
                return render(request, 'up_pwd.html', {'user': user})
            else:
                return render(request,{'mcg':'密码输入有误'})
        else:
            return render(request, 'login.html')
