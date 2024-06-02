from django.shortcuts import render
from .models import Wishlist
from .serializers import WishlistSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import WishlistSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
# Create your views here.
class WishlistView(ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    parser_classes = (MultiPartParser, FormParser)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user_id',]
    ordering_fields = ['-created_at']
    pagination_class = PageNumberPagination
