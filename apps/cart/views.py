from rest_framework import generics

from .models import Cart
from .serializers import CartSerializer

class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

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

