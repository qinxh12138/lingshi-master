import xadmin

# 全局配置
from xadmin import views
# 开启主题修改
from apps.index.models import *


class BaseStyleSettings:
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseStyleSettings)


class GlobalSettings:
    site_title = '零食网后台管理系统'
    site_footer = '千锋互联科技有限公司'
    menu_style = 'accordion'  # 后台菜单样式修改


xadmin.site.register(views.CommAdminView, GlobalSettings)


class ShopAdmin:
    # 默认情况下显示object对象
    list_display = ['shop_id', 'name', 'quantity']
    # 修改分页的默认的条数
    list_per_page = 10
    # 搜索字段
    search_fields = ['shop_id', 'name']
    list_editor = []


xadmin.site.register(Shop, ShopAdmin)


class ShopPropertyAdmin:
    # 默认情况下显示object对象
    list_display = ['shop_id', 'shop_value']
    # 修改分页的默认的条数
    list_per_page = 10
    # 搜索字段
    search_fields = ['shop_value']
    list_editor = []


xadmin.site.register(ShopProperty, ShopPropertyAdmin)


class CategoryAdmin:
    list_display = ['cate_id', 'cate_name']
    # 修改分页的默认的条数
    list_per_page = 10
    # 搜索字段
    search_fields = ['cate_id', 'cate_name']
    list_editor = []


xadmin.site.register(Category, CategoryAdmin)


class SubCateAdmin:
    list_display = ['sub_cate_id', 'name']
    # 修改分页的默认的条数
    list_per_page = 10
    # 搜索字段
    search_fields = ['sub_cate_id', 'name']
    list_editor = []


xadmin.site.register(SubCate, SubCateAdmin)


class BannerAdmin:
    list_display = ['nav_id', 'image_url']
    # 修改分页的默认的条数
    list_per_page = 10
    # 搜索字段
    search_fields = ['image_url']
    list_editor = []


xadmin.site.register(Banner, BannerAdmin)


class ShopCarAdmin:
    list_display = ['car_id', 'shop_number', 'shop_id', 'user_id']
    # 修改分页的默认的条数
    list_per_page = 10
    # 搜索字段
    search_fields = ['car_id', 'shop_number', 'shop_id', 'user_id']
    list_editor = []


xadmin.site.register(ShopCar, ShopCarAdmin)


class ShopImageAdmin:
    list_display = ['image_id', 'img_url', 'shop_id']
    # 修改分页的默认的条数
    list_per_page = 10
    # 搜索字段
    search_fields = ['image_id', 'img_url']
    list_editor = []


xadmin.site.register(ShopImage, ShopImageAdmin)


class OrderAdmin:
    list_display = ['oid', 'order_code', 'price', 'message', ]
    # 修改分页的默认的条数
    list_per_page = 10
    # 搜索字段
    search_fields = ['oid', 'order_code','price', 'message', ]
    list_editor = []


xadmin.site.register(Order, OrderAdmin)


class CommentAdmin:
    list_display = ['comment_id', 'content', 'shop_id', 'user_id']
    # 修改分页的默认的条数
    list_per_page = 10
    # 搜索字段
    search_fields = ['comment_id', 'content', 'shop_id', 'user_id']
    list_editor = []


xadmin.site.register(Comment, CommentAdmin)

# 自定义的admin
from xadmin.plugins import auth


# 显示自定义的方式
class UserAdmin(auth.UserAdmin):
    list_display = ['id', 'username', 'email','phone']


# 先注销
xadmin.site.unregister(User)
# 在注册
xadmin.site.register(User, UserAdmin)
