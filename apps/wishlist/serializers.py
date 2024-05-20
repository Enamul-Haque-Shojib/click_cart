from rest_framework import serializers
from .models import Wishlist

class ProductSerializer(serializers.ModelSerializer):
    pass


class WishlistSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Wishlist
        fields = '__all__'