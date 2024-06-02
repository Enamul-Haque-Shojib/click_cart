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
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser, FormParser


class SizeListCreateView(ListCreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializers


class SizeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializers


class ColorListCreateView(ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializers


class ColorRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializers


# class ProductsViewSet(ModelViewset):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers
    
#     parser_classes = (MultiPartParser, FormParser)
    
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     filterset_class = ProductFilter
#     search_fields = ['title', 'summary', 'description']
#     ordering_fields = ['price']
#     pagination_class = PageNumberPagination


class ProductAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    filterset_class = ProductFilter
    search_fields = ['title', 'summary', 'description']
    ordering_fields = ['price']

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        
        # Filtering
        filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
        for backend in list(filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)

        # Pagination
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = ProductSerializers(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = ProductSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    parser_classes = (MultiPartParser, FormParser)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'summary', 'description']
    ordering_fields = ['price']
    

class ParentCategoryListCreateView(ListCreateAPIView):
    queryset = ParentCategory.objects.all()
    serializer_class = ParentCategorySerializers


class ParentCategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ParentCategory.objects.all()
    serializer_class = ParentCategorySerializers


class SubCategoryListCreateView(ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializers


class SubCategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializers


class ProductQueryListCreateAPIView(ListCreateAPIView):
    queryset = ProductQuery.objects.all()
    serializer_class = ProductQuerySerializers


class ProductQueryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ProductQuery.objects.all()
    serializer_class = ProductQuerySerializers


class ReviewListCreateView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer