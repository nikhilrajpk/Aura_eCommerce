# Generated by Django 5.1.1 on 2024-10-16 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0003_product_sold_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sold_count',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
