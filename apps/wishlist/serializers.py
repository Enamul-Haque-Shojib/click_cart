from rest_framework import serializers
from .models import Wishlist
from apps.product.serializers import ProductSerializers


class WishlistSerializer(serializers.ModelSerializer):
    products = ProductSerializers(many=True, read_only=True)

    class Meta:
        model = Wishlist
        fields = '__all__'