# Generated by Django 5.0.7 on 2024-08-13 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_about_alter_product_sale_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='picture',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
