from django.urls import path
from . import views

urlpatterns = [
    path('', views.WishlistListCreateView.as_view(), name='wishlist-list-create'),
    path('<int:pk>/', views.WishlistDetailView.as_view(), name='wishlist-detail'),
]