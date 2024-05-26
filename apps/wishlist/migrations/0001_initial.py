# Generated by Django 5.0.1 on 2024-05-24 15:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0004_alter_productimage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('wishlist_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('products', models.ManyToManyField(related_name='wishlists', to='product.product')),
            ],
        ),
    ]