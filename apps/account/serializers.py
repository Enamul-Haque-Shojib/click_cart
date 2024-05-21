from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from apps.account.models import CustomerProfile, VendorProfile
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    # gender = serializers.CharField(required=False)
    # phone_number = serializers.CharField(required=False)
    # profile_photo = serializers.ImageField(required=False)
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField(source="get_full_name")
    role = serializers.SerializerMethodField(source="user.role")
    
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "full_name",
            "role"
        ]

    def get_first_name(self, obj):
        return obj.first_name.title()

    def get_last_name(self, obj):
        return obj.last_name.title()

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
        if instance.is_superuser:
            representation["admin"] = True
        return representation


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["username", "email", "first_name", "last_name", "password", 'role']


class CustomerProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = "__all__"


class VendorProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = VendorProfile
        fields = "__all__"


class UpdateCustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = "__all__"


class UpdateVendorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProfile
        fields = "__all__"