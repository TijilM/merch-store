# Generated by Django 4.1.4 on 2022-12-25 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_product_image_url_product_for_user_positions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='accept_orders',
            field=models.BooleanField(default=True),
        ),
    ]