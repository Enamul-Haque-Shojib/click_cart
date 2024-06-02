# Generated by Django 4.2.13 on 2024-05-31 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_productimage_image'),
        ('cart', '0002_remove_cart_product_cart_user_id_cartitem_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
