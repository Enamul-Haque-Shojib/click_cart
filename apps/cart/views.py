from rest_framework import generics, serializers
from .models import Cart,CartItem
from .serializers import CartSerializer,CartItemSerializer
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.account.models import User

# class CartListCreateView(generics.ListCreateAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer

# class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer

class CartItemView(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    parser_classes = (MultiPartParser, FormParser)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user_id',]
    ordering_fields = ['-created_at']
    pagination_class = PageNumberPagination

class CartItemDetailView(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    parser_classes = (MultiPartParser, FormParser)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = PageNumberPagination




# Create your views here.

    



# class CartItemListCreateView(generics.ListCreateAPIView):
#     serializer_class = CartSerializer

#     def get_queryset(self):
#         return CartSerializer.objects.filter(cart_id=self.kwargs['cart_id'])

#     def perform_create(self, serializer):
#         cart = Cart.objects.get(pk=self.kwargs['cart_id'])
#         serializer.save(cart=cart)

# class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = CartSerializer

#     def get_queryset(self):
#         return CartSerializer.objects.filter(cart_id=self.kwargs['cart_id'])


# class CartItemsList(APIView):
#     def get(self, request, format=None):
#         # user_cart = Cart.objects.get(user_id=request.user_id)
#         # items = CartItem.objects.filter(cart=user_cart)
#         items=[]
#         serializer = CartSerializer(items, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         print("called")
#         data = request.data
#         user_id=data['user_id']
#         user = User.objects.filter(user_id=user_id)
#         cart=Cart.objects.get_or_create(data)
#         print(cart_id)
#         serialize_data['cart_id']=cart_id
#         serialize_data['product']=data['product']
#         serialize_data['quantity']=data['quantity']
#         serializer = CartSerializer(data=serialize_data)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CartItemDetails(APIView):
#     def patch(self, request, pk, format=None):
#         item = get_object_or_404(CartItem.objects.all(), pk=pk)
#         if item:
#             data=item.quanty+1
#         serializer = ItemSerializer(item, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         item = get_object_or_404(CartItem.objects.all(), pk=pk)
#         item.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
