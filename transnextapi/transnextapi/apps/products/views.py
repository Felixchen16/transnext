from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from .models import Products
from .serializers import ProductsModelSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ProductsListAPIView(ListAPIView):

    queryset = Products.objects.filter(is_show=True, is_deleted=False).order_by("order", "id")
    serializer_class = ProductsModelSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'category', 'general_category')
