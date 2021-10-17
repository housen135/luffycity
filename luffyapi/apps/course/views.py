from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.serializers import ModelSerializer
from . import models, serializers
from rest_framework.filters import OrderingFilter, SearchFilter
from .filters import CouresFilterSet
from .paginations import CoursePageNumberPagination


class FreeCourseListAPIView(ListAPIView):
    queryset = models.Course.objects.filter(
        is_delete=False, is_show=True).order_by('-orders').all()
    serializer_class = serializers.FreeCourseModelSerializer

    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    ordering_fields = ['price', 'id', 'students']
    search_fields = ['name', 'brief']
    filter_class = CouresFilterSet
    pagination_class = CoursePageNumberPagination


class CategoryListAPIView(ListAPIView):
    queryset = models.CourseCategory.objects.filter(is_delete= False,is_show=True).all()
    serializer_class = serializers.CategorySerializer


class FreeCourseRetrieveAPIView(RetrieveAPIView):
    queryset = models.Course.objects.filter(is_delete = False,is_show=True).all()
    serializer_class =serializers.FreeCourseModelSerializer 


class ChapterListAPIView(ListAPIView):
    queryset = models.CourseChapter.objects.filter(is_delete=False,is_show=True).all()
    serializer_class = serializers.ChapterModelSerializer

    filter_backends =[DjangoFilterBackend]
    filter_fields =['course']




# Create your views here.
