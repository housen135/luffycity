from rest_framework.filters import BaseFilterBackend

class LimitFilter(BaseFilterBackend):
    def filter_queryset(self,request,queryset,view):
        limit = request.query_parmas.get('limit')
        try:
            return queryset[:int(limit)]
        except:
            return queryset
    

from django_filters.rest_framework.filterset import FilterSet
from django_filters import filters

from . import models

class CouresFilterSet(FilterSet):
    max_price = filters.NumberFilter(field_name = 'price',lookup_expr='lte')
    min_price = filters.NumberFilter(field_name='price',lookup_expr='gte')
    class Meta:
        model = models.Course
        fields = ['course_category','max_price','min_price']