from django.db import models
from django.utils import timezone
from django.conf import settings
from apps.product.models import Product
from apps.account.models import User


# *******Wishlist Section*********
class Wishlist(models.Model):
    wishlist_id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='wishlist_item')
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Wishlist {self.id} for {self.user.username}"

