# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-02-12 14:31
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('icon', models.ImageField(default='static/images/1.jpg', upload_to='upload/img/%Y%m%d', verbose_name='头像')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户管理',
                'verbose_name_plural': '用户管理',
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('addr_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='地址ID')),
                ('receiver', models.CharField(max_length=64, verbose_name='收货人')),
                ('province', models.CharField(max_length=20, verbose_name='省份')),
                ('city', models.CharField(max_length=20, verbose_name='城市')),
                ('area', models.CharField(max_length=20, verbose_name='地区')),
                ('detail_address', models.CharField(max_length=255, verbose_name='详细地址')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('status', models.BooleanField(default=1)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '地址',
                'verbose_name_plural': '地址',
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('nav_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='轮播图ID')),
                ('image_url', models.CharField(max_length=255, verbose_name='图片地址')),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
                'db_table': 'banner',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cate_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='分类ID')),
                ('cate_name', models.CharField(max_length=64, verbose_name='分类名称')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='评论ID')),
                ('content', models.CharField(max_length=4000, verbose_name='评论内容')),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('oid', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='订单ID')),
                ('order_code', models.CharField(max_length=64, verbose_name='订单编号')),
                ('price', models.CharField(max_length=64, verbose_name='总金额')),
                ('message', models.CharField(max_length=255, verbose_name='备注信息')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('pay_time', models.CharField(max_length=64)),
                ('confirm_time', models.CharField(max_length=64)),
                ('status', models.IntegerField(default=1)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '商品订单',
                'verbose_name_plural': '商品订单',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shop_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='商品ID')),
                ('name', models.CharField(max_length=255, verbose_name='食品名称')),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='商品原价')),
                ('promote_price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='折扣价')),
                ('stock', models.IntegerField(verbose_name='库存')),
                ('quantity', models.IntegerField(default=0, verbose_name='销量')),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'db_table': 'shop',
            },
        ),
        migrations.CreateModel(
            name='ShopCar',
            fields=[
                ('car_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='购物车ID')),
                ('shop_number', models.IntegerField(verbose_name='商品数量')),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('shop_id', models.ForeignKey(db_column='shop_id', on_delete=django.db.models.deletion.CASCADE, to='index.Shop', verbose_name='商品')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
                'db_table': 'shop_car',
            },
        ),
        migrations.CreateModel(
            name='ShopImage',
            fields=[
                ('image_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='图片ID')),
                ('img_url', models.CharField(max_length=255, verbose_name='图片地址')),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('shop_id', models.ForeignKey(db_column='shop_id', on_delete=django.db.models.deletion.CASCADE, to='index.Shop', verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品图片',
                'verbose_name_plural': '商品图片',
                'db_table': 'shop_image',
            },
        ),
        migrations.CreateModel(
            name='ShopProperty',
            fields=[
                ('property_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='商品属性ID')),
                ('shop_value', models.CharField(max_length=255, verbose_name='商品属性')),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('shop_id', models.ForeignKey(db_column='shop_id', on_delete=django.db.models.deletion.CASCADE, to='index.Shop', verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品属性',
                'verbose_name_plural': '商品属性',
                'db_table': 'shop_property',
            },
        ),
        migrations.CreateModel(
            name='SubCate',
            fields=[
                ('sub_cate_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='二级菜单ID')),
                ('name', models.CharField(max_length=64, verbose_name='名称')),
                ('cate_id', models.ForeignKey(db_column='cate_id', on_delete=django.db.models.deletion.CASCADE, to='index.Category')),
            ],
            options={
                'verbose_name': '二级菜单',
                'verbose_name_plural': '二级菜单',
                'db_table': 'sub_cate',
            },
        ),
        migrations.AddField(
            model_name='shop',
            name='sub_cate_id',
            field=models.ForeignKey(db_column='sub_cate_id', on_delete=django.db.models.deletion.CASCADE, to='index.SubCate'),
        ),
        migrations.AddField(
            model_name='comment',
            name='shop_id',
            field=models.ForeignKey(db_column='shop_id', on_delete=django.db.models.deletion.CASCADE, to='index.Shop', verbose_name='商品'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]