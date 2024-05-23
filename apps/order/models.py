import uuid
from django.db import models
from django.utils import timezone
from apps.account.models import CustomerProfile
from apps.product.models import Product

class Order(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name='orders')
    payment_status = models.CharField(max_length=20, default='Pending')
    order_status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(default=timezone.now)
    shipping_address = models.CharField(max_length=255)
    billing_address = models.CharField(max_length=255)

    def __str__(self):
        return f"Order {self.order_id} by {self.customer.user.username}"

class OrderItem(models.Model):
    item_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.FloatField()

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"
