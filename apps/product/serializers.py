from rest_framework import serializers
from apps.product.models import (ParentCategory, SubCategory, Size, Color, 
                                 Product, ProductImage, ProductQuery, Review)


class ParentCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = ParentCategory
        fields = "__all__"


class SubCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"


class SizeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"


class ColorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"


class ProductsImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class ProductSerializers(serializers.ModelSerializer):
    images = ProductsImageSerializers(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Product
        fields = ["product_id", "title", "category", "size", "color", "summary",
                  "description", "price", "quantity", "discount_price", 
                  "images", "uploaded_images", "vendor"
                  ]

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        product = Product.objects.create(**validated_data)

        for image in uploaded_images:
            ProductImage.objects.create(product=product, image=image)

        return product


class ProductQuerySerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductQuery
        fields = [
            'product', 'customer', 'comment'
        ]


class ReviewSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(many=False)
    customer = serializers.StringRelatedField(many=False)

    class Meta:
        model = Review
        fields = [
            'product', 'customer', 'rating', 'comment'
        ]