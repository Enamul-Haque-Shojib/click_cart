"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/cart/", include("apps.cart.urls")),
    path("api/v1/wishlist/", include("apps.wishlist.urls")),
    path("api/v1/profile/", include("apps.account.urls")),
    path("api/v1/products/", include("apps.product.urls")),
    path("api/v1/", include("apps.transaction.urls")),
    path("api/v1/orders/", include("apps.order.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Click Cart Admin"
admin.site.site_title = "Click Cart Admin Portal"
admin.site.index_title = "Welcome to the Click Cart Portal"
