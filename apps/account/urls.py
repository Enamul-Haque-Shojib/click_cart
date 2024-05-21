from django.urls import path

from .views import (GetCustomerProfileAPIView, UpdateCustomerProfileAPIView, 
                    GetVendorProfileAPIView, UpdateVendorProfileAPIView)

urlpatterns = [
    path("customer/me/", GetCustomerProfileAPIView.as_view(), name="get_customer_profile"),
    path("vendor/me/", GetCustomerProfileAPIView.as_view(), name="get_vendor_profile"),
    path(
        "customer/update/<str:username>/", UpdateCustomerProfileAPIView.as_view(), name="update_customer_profile"
    ),
    path(
        "vendor/update/<str:username>/", UpdateVendorProfileAPIView.as_view(), name="update_vendor_profile"
    ),
]
