from django.shortcuts import render, get_object_or_404
from .filters import ProductFilter
from apps.product.models import (ParentCategory, SubCategory, ProductQuery, 
                                 Product, Review, Size, Color)
from apps.product.serializers import (SizeSerializers, ColorSerializers, 
                                      ParentCategorySerializers, 
                                      SubCategorySerializers,
                                      ProductSerializers, 
                                      ProductQuerySerializers,
                                      ReviewSerializer
                                      )
from rest_framework.generics import (RetrieveUpdateDestroyAPIView, 
                                     ListCreateAPIView)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser, FormParser


class SizeViewset(ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializers


class ColorViewset(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializers


class ProductsViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
    parser_classes = (MultiPartParser, FormParser)
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'summary', 'description']
    ordering_fields = ['old_price']
    pagination_class = PageNumberPagination


class ParentCategoryViewset(ModelViewSet):
    queryset = ParentCategory.objects.all()
    serializer_class = ParentCategorySerializers


class SubCategoryViewset(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializers


class ProductQueryViewset(ModelViewSet):
    queryset = ProductQuery.objects.all()
    serializer_class = ProductQuerySerializers


class ReviewListCreateView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer