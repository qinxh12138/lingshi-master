from django.db.models import Sum

from apps.index.models import *


def shop_count(request):
    count = 0
    if request.user.is_authenticated():
        count = ShopCar.objects.filter(user_id=request.user.id, is_delete=0).aggregate(
            sum=Sum('shop_number')).get('sum')
    return {'count': count}
