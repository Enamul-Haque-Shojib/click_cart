from django.db import models
from django.utils import timezone
from django.conf import settings


# *******Wishlist Section*********
class Wishlist(models.Model):
    wishlist_id = models.AutoField(primary_key=True, editable=False)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='wishlists')
    created_at = models.DateTimeField(timezone.now)

    def __str__(self):
        return f"Wishlist {self.id} for {self.user.username}"