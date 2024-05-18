from django.db import models

# Create your models here.
class Cart(models.Model):
    ProductID = models.ForeignKey(Account, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str(self):
        return self.ProductID