import uuid
from django.db import models
from django.utils import timezone
from apps.account.models import CustomerProfile, VendorProfile


class ParentCategory(models.Model):
    parent_category_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    parent_category = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.parent_category
    

class SubCategory(models.Model):
    sub_category_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    parent = models.ForeignKey(ParentCategory, on_delete=models.CASCADE, null=True, blank=True)
    sub_category = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sub_category


class Size(models.Model):
    product_size = models.CharField(max_length=30)

    def __str__(self):
        return self.product_size


class Color(models.Model):
    product_color = models.CharField(max_length=30)
    
    def __str__(self):
        return self.product_color


class Product(models.Model):
    product_id = models.UUIDField(
        default=uuid.uuid4, editable=False, primary_key=True, unique=True
    )
    title = models.CharField(max_length=50)
    slug = models.SlugField(default=None, blank=True, null=True)
    category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, null=True, blank=True
    )
    product_image = models.ImageField(upload_to='product/images/')
    size = models.ManyToManyField(
        Size, default=None, blank=True
    )
    color = models.ManyToManyField(
        Color, default=None, blank=True
    )
    summary = models.TextField(default="Write Something...") 
    description = models.TextField(default="Write Something...")
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    discount_price = models.FloatField(default=0.0)
    flash_sales = models.BooleanField(default=False)
    vendor = models.ForeignKey(
        VendorProfile, on_delete=models.CASCADE, null=True, blank=True
    )
    created_at = models.DateTimeField(timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(
        upload_to="product/media/uploads/", default="", null=True, blank=True
    )

    def __str__(self):
        return "%s" % (self.product.name)


class ProductQuery(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True
    )
    customer = models.ForeignKey(
        CustomerProfile, on_delete=models.CASCADE, null=True, blank=True
    )
    comment = models.TextField(default="Write here...")

    def __str__(self):
        return f"{self.user.user.username} commented"


STAR_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews'
    )
    customer = models.ForeignKey(
        CustomerProfile, on_delete=models.CASCADE, null=True, blank=True
    )
    rating = models.CharField(choices=STAR_CHOICES, max_length=10)
    comment = models.TextField()
    created = models.DateTimeField(timezone.now)

    def __str__(self):
        return f"{self.customer.user.username} reviewed"