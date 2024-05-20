from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartListCreateView.as_view(), name='cart-list-create'),
    path('<uuid:pk>/', views.CartDetailView.as_view(), name='cart-detail'),
]
