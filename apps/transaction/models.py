from django.db import models
from apps.account.models import User
# Create your models here.

class Transaction(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id=models.IntegerField()
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    # transaction_type = models.
    # transaction_status=model.
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    