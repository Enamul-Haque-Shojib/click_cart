from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.CartListCreateView.as_view(), name='cart-list-create'),
    path('cart/<int:pk>/', views.CartDetailView.as_view(), name='cart-detail'),
    path('cart/<int:cart_id>/items/', views.CartItemListCreateView.as_view(), name='cart-item-list-create'),
    path('cart/<int:cart_id>/items/<int:pk>/', views.CartItemDetailView.as_view(), name='cart-item-detail'),
]
