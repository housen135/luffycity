
from django import http
from django.core.cache import cache
from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from . import serializers
from utils.response import APIResponse
from libs import tx_sms

from django.conf import settings
from . import models

import re

#普通登录接口
class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = serializers.LoginModelSerializer(data=request.data)
        if serializer.is_valid():
            print('登录成功')
            return APIResponse(data={
                'username': serializer.user.username,
                'token': serializer.token
            })
        print('LoginAPIview--->',serializer.errors)
        return APIResponse(1, 'failed', data=serializer.errors, http_status=400)

#验证码接口
from . import throttles
class SMSAPIView(APIView):
    throttle_classes = [throttles.SMSThrottle]
    def post(self, request, *args, **kwargs):
        mobile = request.data.get('mobile')
        if not(mobile and re.match(r'^1[3-9][0-9]{9}$', mobile)):
            return APIResponse(data_status=2, data_msg='SMSview手机格式有误')
        code = tx_sms.get_code()
        result = tx_sms.send_sms(mobile, code, settings.SMS_EXP)
        if result == 0:
            print('SMS------>短信发送失败')
            return APIResponse(data_status=1, data_msg='短信发送失败5')


        cache.set(settings.SMS_CACHE_KEY % mobile, code, settings.SMS_EXP)
        return APIResponse(data_status=0,data_msg='短信发送成功')

#短信登录接口
class LoginMobileAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = serializers.LoginMobileSerializer(data=request.data)
        if serializer.is_valid():
            return APIResponse(data={
                'username': serializer.user.username,
                'token': serializer.token
            })
        print('LoginMobileAPIview--->',serializer.errors)
        return APIResponse(1,data_msg='登陆失败LoginMobile',data=serializer.errors,http_status=200)


# 校验手机接口
class MobileAPIView(APIView):
    authentication_classes=[]
    permission_classes=[]
    def post(self,request,*args,**kwargs):
        mobile = request.data.get('mobile')
        if not(mobile and re.match(r'^1[3-9][0-9]{9}',mobile)):

            return APIResponse(2,'手机格式有误',http_status = 400)
        try:
            result=models.User.objects.get(mobile = mobile)
            print('mobileapiview---->',result)
            
            print('mobileapiview','手机已经注册')
            return APIResponse(1,'手机已经注册')
        except Exception as e:
            return APIResponse(0,'手机未注册') # 报错反而是对的

            
#注册接口
class RegisterAPIView(APIView):
    authentication_classes=[]
    permission_classes = []
    def post(self,request,*args,**kwargs):
        serializer = serializers.RegisterMobileSerializer(data = request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return APIResponse(0,data_msg='注册成功',data={
                'username':obj.username,
                'mobile':obj.mobile,
                'email':obj.email
            })
        print('RegisterAPIview--->',serializer.errors)
        return APIResponse(1,'注册失败',data=serializer.errors,http_status=400)




# Create your views here.
