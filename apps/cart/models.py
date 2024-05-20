from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Product(models.Model):
    pass

class Cart(models.Model):
    cart_id = id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str(self):
        return self.ProductID
    


# *********CartItem Section**********    
class CartItem(models.Model):
    cart_item_id = models.AutoField(primary_key=True, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(timezone.now)

    def __str__(self):
        return f"Item {self.cart_item_id} in Cart {self.cart.id}"
    



