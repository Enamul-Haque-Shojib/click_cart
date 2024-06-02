# from django.urls import path
# from . import views

# urlpatterns = [
#     # path('', views.CartListCreateView.as_view(), name='cart-list-create'),
#     # path('<uuid:pk>/', views.CartDetailView.as_view(), name='cart-detail'),
#     path('', views.CartItemsList.as_view(), name=""),
#     path('<uuid:pk>/', views.CartItemDetails.as_view(), name=""),
# ]
from django.urls import path, include
from apps.cart.views import CartItemView,CartItemDetailView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("carts", CartItemView)
router.register("cart", CartItemDetailView)

urlpatterns = [
    path("", include(router.urls)),    
]