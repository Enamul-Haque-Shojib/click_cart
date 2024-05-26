from django.urls import path, include
from apps.transaction.views import TransactionViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("transactions", TransactionViewSets)

urlpatterns = [
    path("", include(router.urls)),    
]