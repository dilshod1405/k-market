# Generated by Django 5.0.7 on 2024-08-08 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_order_address_order_count_order_serial_number_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sity',
            new_name='City',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='sity',
            new_name='city',
        ),
    ]
