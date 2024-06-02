from django.db import models
from django.utils import timezone
from django.conf import settings
from apps.product.models import Product
from apps.account.models import User


# *******Wishlist Section*********
class Wishlist(models.Model):
    wishlist_id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist_item')
    products = models.ManyToManyField(Product, related_name='wishlists')
    created_at = models.DateTimeField(timezone.now)

    def __str__(self):
        return f"Wishlist {self.id} for {self.user.username}"