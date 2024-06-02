from django.db import models
from django.utils import timezone
from django.conf import settings
from apps.product.models import Product
import uuid
from apps.account.models import User

# Create your models here.

class Cart(models.Model):
    cart_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, unique=True,related_name='user_cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str(self):
        return self.user_id
    


# *********CartItem Section**********    
class CartItem(models.Model):
    cart_item_id = models.AutoField(primary_key=True, editable=False)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Item {self.cart_item_id} in Cart {self.cart.id}"
    



