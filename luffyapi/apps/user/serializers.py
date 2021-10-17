
from django.conf import settings
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from django.core.cache import cache

from . import models

import re


class LoginModelSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = models.User
        fields = ('username', 'password')

    def validate(self, attrs):
        user = self._many_method_login(**attrs)
        if not user:
            raise ValueError({'user': '错误'})
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        self.user = user
        self.token = token
        return attrs

    def _many_method_login(self, **attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if re.match(r'^1[3-9][0-9]{9}$', username):
            user = models.User.objects.filter(mobile=username).first()
        if re.match(r'.*@.*', username):
            user = models.User.objects.filter(emial=username).first()
        else:
            user = models.User.objects.filter(username=username).first()
        if not user:
            raise ValidationError({'username': 'loginmodelser账号有误'})
        if not user.check_password(password):
            raise ValidationError({'password': 'loginmodelser密码错误'})
        return user


class LoginMobileSerializer(serializers.ModelSerializer):
    mobile = serializers.CharField(
        write_only=True, min_length=11, max_length=11)
    code = serializers.CharField(write_only=True, min_length=3, max_length=3)

    class Meta:
        model = models.User
        fields = ('mobile', 'code')

    def validate_mobile(self, value):
        if re.match(r'^1[3-9][0-9]{9}', value):
            return value
        raise serializers.ValidationError('LoginMobileSer手机不符合格式')

    def validate_code(self, value):
        try:
            int(value) and len(value) == 3
            return value
        except:
            raise serializers.ValidationError('LoginMobileSer验证码格式不对')

    def validate(self, attrs):
        user = self._get_user(**attrs)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        self.user = user
        self.token = token
        return attrs

    def _get_user(self, **attrs):
        mobile = attrs.get('mobile')
        code = attrs.get('code')
        user = models.User.objects.filter(mobile=mobile).first()
        if not user:
            raise serializers.ValidationError('LoginMobileSer此手机号未注册')
        old_code = cache.get(settings.SMS_CACHE_KEY % mobile)
        if code != old_code:
            raise serializers.ValidationError('LoginMobileSer验证码不正确')
        return user

class RegisterMobileSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length =3,min_length=3)
    class Meta:

        model=models.User
        fields =('mobile','password','code')
        extra_kwargs ={
            'mobile':{
                'min_length':11,
                'max_length':11,
            },
            'password':{
                'min_length':3,
                'max_length':10,

            }
        }
    def validate_mobile(self,value):
        if re.match(r'^1[3-9][0-9]{9}',value):
            return value
        raise serializers.ValidationError('RegMobileSer手机格式有误')


    def validate_password(self,value):
        return value
        
    def validate_code(self,value):
        try:
            int(value)
            return value
        except:
            raise serializers.ValidationError('RegMobileSer验证码格式有误')

    def validate(self,attrs):
        mobile = attrs.get('mobile')
        code = attrs.pop('code')
        old_code = cache.get(settings.SMS_CACHE_KEY % mobile)
        if code != old_code:
            raise serializers.ValidationError({'code':'RegMobileSer验证码有误'})

        attrs['username']=mobile
        attrs['email']='%s@oldboy.colm'%mobile
        return attrs
    
    def create(self,validate_data):
        return models.User.objects.create_user(**validate_data)

        

