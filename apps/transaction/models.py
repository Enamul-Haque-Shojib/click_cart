from django.db import models
from apps.account.models import User
from apps.order.models import Order
# Create your models here.

TRANSACTION_TYPE=[
    ("COD","COD"),
    ("ONLINE","ONLINE"),
]
TRANSACTION_STATUS=[
    ("PENDING","PENDING"),
    ("PAID","PAID"),
    ("CANCELLED","CANCELLED")
]

class Transaction(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id=models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    transaction_type = models.CharField(choices=TRANSACTION_TYPE,max_length=20, default="COD")
    transaction_status=models.CharField(choices=TRANSACTION_STATUS,max_length=20, default="PENDING")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    