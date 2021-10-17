from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from . import models
from . import serializers
from django.core.cache import cache


class BannerListAPIView(ListAPIView):
    queryset = models.Banner.objects.filter(is_delete = False,is_show =True).order_by('-order').all()
    serializer_class = serializers.BannerModelSerializer



    def get(self,request,*args,**kwargs):
        banner_list = cache.get('banner_list')
        if not banner_list:
            print('走数据库了')
            response = self.list(request,*args,**kwargs)
            print('response------->',response)
            cache.set('banner_list',response.data)
            return response
        return Response(banner_list)

    pass
# Create your views here.
 