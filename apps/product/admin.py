from django.contrib import admin
from apps.product.models import (Product, ProductQuery, ParentCategory, Review,
                                 SubCategory, Size, Color)
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductQuery)
admin.site.register(ParentCategory)
admin.site.register(SubCategory)
admin.site.register(Review)
admin.site.register(Size)
admin.site.register(Color)
