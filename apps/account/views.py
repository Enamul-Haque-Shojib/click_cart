from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import NotYourProfile, ProfileNotFound
from .models import CustomerProfile, VendorProfile
from .renderers import ProfileJSONRenderer
from .serializers import CustomerProfileSerializers, UpdateCustomerProfileSerializer
from .serializers import VendorProfileSerializers, UpdateVendorProfileSerializer


class GetCustomerProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]

    def get(self, request):
        user = self.request.user
        user_customerprofile = CustomerProfile.objects.get(user=user)
        serializer = CustomerProfileSerializers(user_customerprofile, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateCustomerProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]

    serializer_class = UpdateCustomerProfileSerializer

    def patch(self, request, username):
        try:
            CustomerProfile.objects.get(user__username=username)
        except CustomerProfile.DoesNotExist:
            raise ProfileNotFound

        user_name = request.user.username
        if user_name != username:
            raise NotYourProfile

        data = request.data
        serializer = UpdateCustomerProfileSerializer(
            instance=request.user.customerprofile, data=data, partial=True
        )

        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class GetVendorProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]

    def get(self, request):
        user = self.request.user
        user_vendorprofile = VendorProfile.objects.get(user=user)
        serializer = VendorProfileSerializers(user_vendorprofile, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateVendorProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]

    serializer_class = UpdateVendorProfileSerializer

    def patch(self, request, username):
        try:
            VendorProfile.objects.get(user__username=username)
        except VendorProfile.DoesNotExist:
            raise ProfileNotFound

        user_name = request.user.username
        if user_name != username:
            raise NotYourProfile

        data = request.data
        serializer = UpdateVendorProfileSerializer(
            instance=request.user.vendorprofile, data=data, partial=True
        )

        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)