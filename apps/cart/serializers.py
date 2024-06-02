from rest_framework import serializers
from .models import Cart
from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    cart_id = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all(), 
                                                  many=False)
    class Meta:
        model = CartItem
        fields = '__all__'



class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ['cart_id','user_id','cart_items']


