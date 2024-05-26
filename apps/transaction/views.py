from django.shortcuts import render
from apps.transaction.models import Transaction
from apps.transaction.serializers import TransactionSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class TransactionViewSets(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializers
    parser_classes = (MultiPartParser, FormParser)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user_id', 'order_id']
    ordering_fields = ['-created_at']
    pagination_class = PageNumberPagination

    