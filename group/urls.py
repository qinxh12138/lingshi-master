from django.conf.urls import url, include
import xadmin
from django.conf.urls.static import static
from django.contrib import admin

from apps.index import views
from group import settings
from apps.index import search_views

urlpatterns = [
                  url(r'^xadmin/', xadmin.site.urls),
                  url('user_account/', include('apps.user_account.urls')),
                  url('^$', views.index, name='index'),
                  url('detail/', include('apps.detail.urls')),
                  url('car/', include('apps.car.urls')),
                  url('pay/', include('apps.order.urls')),
                  url('search/', include('apps.search.urls')),
                  url(r'^haystacksearch/', search_views.MySeachView(), name='haystack_search'),
                  url('admin/', admin.site.urls),
                  url('accounts/', include('allauth.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
