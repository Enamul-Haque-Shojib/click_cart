from rest_framework import serializers
from apps.product.models import (ParentCategory, SubCategory, Size, Color, 
                                 Product, ProductImage, ProductQuery, Review)


class ParentCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = ParentCategory
        fields = [
                   "parent_category_id", "parent_category", "created_at", 
                   "updated_at"
                  ]


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
        fields = ["id", "product", "image"]


class ProductSerializers(serializers.ModelSerializer):
    images = ProductsImageSerializers(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Product
        fields = [
            "product_id", "title", "category", "size", "color", "summary", 
            "description", "price", "quantity", "vendor", "created_at",
            "images", "uploaded_images",
        ]

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images", [])
        sizes = validated_data.pop('size', [])
        colors = validated_data.pop('color', [])
        product = Product.objects.create(**validated_data)

        if sizes:
            product.size.set(sizes)  # Using set() to assign many-to-many field

        if colors:
            product.color.set(colors)  # Using set() to assign many-to-many field

        for image in uploaded_images:
            ProductImage.objects.create(product=product, image=image)

        return product
    
    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop("uploaded_images", [])
        sizes = validated_data.pop('size', [])
        colors = validated_data.pop('color', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        if sizes:
            instance.size.set(sizes)  # Using set() to update many-to-many field
            
        if colors:
            instance.color.set(colors)  # Using set() to update many-to-many field

        if uploaded_images:
            instance.images.all().delete()  # Optionally, clear previous images
            for image in uploaded_images:
                ProductImage.objects.create(product=instance, image=image)

        return instance


class ProductQuerySerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductQuery
        fields = [
            'id', 'product', 'customer', 'comment'
        ]


class ReviewSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(many=False)
    customer = serializers.StringRelatedField(many=False)

    class Meta:
        model = Review
        fields = [
            'id', 'product', 'customer', 'rating', 'comment'
        ]