from rest_framework import serializers
from .models import Wishlist
from apps.product.serializers import ProductSerializers


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ['wishlist_id','user','product']