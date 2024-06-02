from django.urls import path, include
from apps.product.views import (ColorListCreateView, 
                                ColorRetrieveUpdateDestroyView,
                                SizeListCreateView,
                                SizeRetrieveUpdateDestroyView,
                                ParentCategoryListCreateView,
                                ParentCategoryRetrieveUpdateDestroyView,
                                SubCategoryListCreateView,
                                SubCategoryRetrieveUpdateDestroyView,
                                ProductAPIView, 
                                ProductRetrieveUpdateDestroyAPIView,
                                ReviewListCreateView, ReviewDetailView, 
                                ProductQueryListCreateAPIView,
                                ProductQueryRetrieveUpdateDestroyView
                                )


urlpatterns = [
    path("", ProductAPIView.as_view(), name="products"),
    path('<uuid:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-details'),
    path('size/', SizeListCreateView.as_view(), name="size"),
    path('size/<int:pk>/', SizeRetrieveUpdateDestroyView.as_view(), name="size-details"),
    path('color/', ColorListCreateView.as_view(), name="color"),
    path('color/<int:pk>/', ColorRetrieveUpdateDestroyView.as_view(), name="color-details"),
    path("parentcategory/", ParentCategoryListCreateView.as_view(), name="parent_category"),
    path('parentcategory/<uuid:pk>/', ParentCategoryRetrieveUpdateDestroyView.as_view(), name='parentcategory-detail'),
    path("subcategory/", SubCategoryListCreateView.as_view(), name="subcategory"),
    path('subcategory/<int:pk>/', SubCategoryRetrieveUpdateDestroyView.as_view(), name='subcategory-detail'),
    path("query/", ProductQueryListCreateAPIView.as_view(), name="product-query"),
    path("query/<int:pk>/",  ProductQueryRetrieveUpdateDestroyView.as_view(), name="query-details"),
    path("reviews/", ReviewListCreateView.as_view(), name="review"),
    path("reviews/<int:pk>/", ReviewDetailView.as_view(), name="review_detail")
]