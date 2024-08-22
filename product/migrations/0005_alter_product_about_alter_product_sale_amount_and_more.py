# Generated by Django 5.0.7 on 2024-08-06 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='about',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_amount',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='serial_number',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
