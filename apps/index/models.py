from django.contrib.auth.models import AbstractUser

from django.db import models


# """
# 给图片重名了
# """
#
#
# class ImageStorage(FileSystemStorage):
#     IMG_PREFIX = 'IMG_'
#     FILE_TIME = time.strftime('%Y%m%d%H%M%S')
#     from django.conf import settings
#
#     def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
#         # 初始化
#         super().__init__(location, base_url)
#         # 重写 _save方法
#
#     # uploaad/img/img_afsfsfds.png
#     # 修改文件的名称
#     def _save(self, name, content):
#         # 文件扩展名
#         ext_name = name[name.rfind('.'):]
#         # 文件目录
#         image_path = os.path.dirname(name)
#         # 定义文件名，年月日时分秒随机数
#         image_name = self.IMG_PREFIX + self.FILE_TIME + ext_name
#         image_file = os.path.join(image_path, image_name)
#         # 调用父类方法
#         return super()._save(image_file, content)


class User(AbstractUser):
    phone = models.CharField(verbose_name='手机号', max_length=11)
    icon = models.ImageField(verbose_name='头像', max_length=100, upload_to='upload/img/%Y%m%d',
                             default=u'static/images/1.jpg')

    class Meta:
        db_table = 'user'
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name

    def img_show(self):
        """
        后台显示图片
        :return:
        """
        return u'<img width=50px src="%s" />' % self.icon.url

    img_show.short_description = u'头像'
    # 允许显示HTML tag
    img_show.allow_tags = True


class Address(models.Model):
    addr_id = models.AutoField(verbose_name='地址ID', primary_key=True, auto_created=True)
    receiver = models.CharField(verbose_name='收货人', max_length=64)
    province = models.CharField(verbose_name='省份', max_length=20)
    city = models.CharField(verbose_name='城市', max_length=20)
    area = models.CharField(verbose_name='地区', max_length=20)
    detail_address = models.CharField(verbose_name='详细地址', max_length=255)
    phone = models.CharField(verbose_name='手机号', max_length=11)
    # 地址表示，1代表默认地址，0代表普通地址
    status = models.BooleanField(default=1)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, db_column='user_id')
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    nav_id = models.AutoField(verbose_name='轮播图ID', primary_key=True, auto_created=True)
    image_url = models.CharField(verbose_name='图片地址', max_length=255)
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'banner'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name


class Category(models.Model):
    cate_id = models.AutoField(verbose_name='分类ID', primary_key=True, auto_created=True)
    cate_name = models.CharField(verbose_name='分类名称', max_length=64)

    class Meta:
        db_table = 'category'
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class SubCate(models.Model):
    sub_cate_id = models.AutoField(verbose_name='二级菜单ID', primary_key=True, auto_created=True)
    name = models.CharField(verbose_name='名称', max_length=64)
    cate_id = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='cate_id', db_index=True)

    class Meta:
        db_table = 'sub_cate'
        verbose_name = '二级菜单'
        verbose_name_plural = verbose_name


class Shop(models.Model):
    shop_id = models.AutoField(verbose_name='商品ID', primary_key=True, auto_created=True)
    name = models.CharField(verbose_name='食品名称', max_length=255)
    original_price = models.DecimalField(verbose_name='商品原价', max_digits=7, decimal_places=2)
    promote_price = models.DecimalField(verbose_name='折扣价', max_digits=7, decimal_places=2)
    stock = models.IntegerField(verbose_name='库存', )
    quantity = models.IntegerField(verbose_name='销量', default=0)
    sub_cate_id = models.ForeignKey(SubCate, on_delete=models.CASCADE, db_column='sub_cate_id', db_index=True)
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shop'
        verbose_name = '商品'
        verbose_name_plural = verbose_name


class ShopProperty(models.Model):
    property_id = models.AutoField(verbose_name='商品属性ID', primary_key=True, auto_created=True)
    shop_value = models.CharField(verbose_name='商品属性', max_length=255)
    shop_id = models.ForeignKey(Shop, verbose_name='商品', on_delete=models.CASCADE, db_column='shop_id', db_index=True)
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shop_property'
        verbose_name = '商品属性'
        verbose_name_plural = verbose_name


class ShopCar(models.Model):
    car_id = models.AutoField(verbose_name='购物车ID', primary_key=True, auto_created=True)
    shop_number = models.IntegerField(verbose_name='商品数量')
    shop_id = models.ForeignKey(Shop, verbose_name='商品', on_delete=models.CASCADE, db_column='shop_id', db_index=True)
    user_id = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE, db_column='user_id', db_index=True)
    #购物车显示  0显示 1删除
    is_delete = models.BooleanField(default=False)
    #订单显示 0显示 1不显示
    status = models.BooleanField(default=True)
    # 购物状态 0未购买 1已经购买
    is_status=models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shop_car'
        verbose_name = '购物车'
        verbose_name_plural = verbose_name


class ShopImage(models.Model):
    image_id = models.AutoField(verbose_name='图片ID', primary_key=True, auto_created=True)
    img_url = models.CharField(verbose_name='图片地址', max_length=255)
    shop_id = models.ForeignKey(Shop, verbose_name='商品', on_delete=models.CASCADE, db_column='shop_id', db_index=True)
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shop_image'
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name


class Order(models.Model):
    oid = models.AutoField(verbose_name='订单ID', primary_key=True, auto_created=True)
    order_code = models.CharField(verbose_name='订单编号', max_length=64)
    price = models.CharField(verbose_name='总金额', max_length=64)
    message = models.CharField(verbose_name='备注信息', max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    pay_time = models.CharField(max_length=64)
    confirm_time = models.CharField(max_length=64)
    # 订单状态：-1代表删除，0代表取消，1代表支付，2代表未支付，3代表完成
    status = models.IntegerField(default=1)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', db_index=True)

    class Meta:
        db_table = 'order'
        verbose_name = '商品订单'
        verbose_name_plural = verbose_name


class Comment(models.Model):
    comment_id = models.AutoField(verbose_name='评论ID', primary_key=True, auto_created=True)
    content = models.CharField(verbose_name='评论内容', max_length=4000)
    shop_id = models.ForeignKey(Shop, verbose_name='商品', on_delete=models.CASCADE, db_column='shop_id', db_index=True)
    user_id = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE, db_column='user_id', db_index=True)
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comment'
        verbose_name = '评论'
        verbose_name_plural = verbose_name
