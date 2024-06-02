from django.urls import path, include
from .views import WishlistView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("wishlists", WishlistView)


urlpatterns = [
    path("", include(router.urls)),    
]