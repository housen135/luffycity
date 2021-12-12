from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
class PayAPIView(APIView):
    authentication_classes = [JSONWebTokenAuthentication]
    print('认证ok')
    permission_classes = [IsAuthenticated]
    def post(self,request,*args,**kwargs):
        serializer = serializers.OrderModelSerializer(data = request.data,context = {'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.pay_url)


from libs.ipay import alipay
from . import models
from utils.logging import logger
class SuccessAPIView(APIView):
    def patch(self,request,*args,**kwargs):
        print('success----->',request.query_params)
        data = request.query_params.dict()
        sign = data.pop('sign')
        result = alipay.verify(data,sign)
        if result:
            models.Order.objects.filter(out_trade_no = data.get('out_trade_no')).update(order_status = 1)
        return Response('success')
        
    def post(self, request, *args, **kwargs):
        data = request.data.dict()  # 回调参数，是QueryDict类型，不能直接调用pop方法
        sign = data.pop('sign')  # 签名
        out_trade_no = data.get('out_trade_no')  # 订单号
        result = alipay.verify(data, sign)
        if result and data["trade_status"] in ("TRADE_SUCCESS", "TRADE_FINISHED" ):
            try:
                order = models.Order.objects.get(out_trade_no=out_trade_no)
                if order.order_status != 1:
                    order.order_status = 1
                    order.save()
                    logger.warning('%s订单完成支付' % out_trade_no)
                return Response('success')
            except:
                pass
        return Response('failed')


    
# Create your views here.
