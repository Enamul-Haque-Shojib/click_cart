from django.urls import path, include
from apps.product.views import (ColorViewset, SizeViewset,
                                ParentCategoryViewset,
                                SubCategoryViewset, ProductsViewSet, 
                                ReviewListCreateView, ReviewDetailView, 
                                ProductQueryViewset)

from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

router = DefaultRouter()
router.register("products", ProductsViewSet)
router.register("parentcategory", ParentCategoryViewset)
router.register("subcategory", SubCategoryViewset)
router.register('colors', ColorViewset)
router.register('sizes', SizeViewset)


product_router = NestedDefaultRouter(router, "products", lookup="product")
product_router.register("queries", ProductQueryViewset, basename="product-query")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(product_router.urls)),
    path("reviews/", ReviewListCreateView.as_view(), name="review"),
    path("reviews/<int:pk>/", ReviewDetailView.as_view(), name="review_detail"),
    
]