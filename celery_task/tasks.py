from .celery import app
import os,django

from home.models import Banner
from django.conf import settings
from home.serializers import BannerModelSerializer
from django.core.cache import cache


@app.task
def update_banner_cache():
    banner_query = Banner.objects.filter(is_delete=False,is_show=True).order_by('-order')
    temp = BannerModelSerializer(banner_query,many=True)
    banner_list = temp.data
    print('data---->',banner_list)
    print('banner_list--------->',BannerModelSerializer(banner_query,many=True))
    for banner_dic in banner_list:
        banner_dic['image'] = settings.BASE_URL+banner_dic['image']

    cache.set('banner_list',banner_list)