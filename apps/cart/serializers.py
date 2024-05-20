from rest_framework import serializers
from .models import Cart
from .models import CartItem

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    cart = CartSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = '__all__'

