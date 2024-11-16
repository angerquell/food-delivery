# Generated by Django 5.1.3 on 2024-11-16 08:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_order_food_order_price_alter_food_calories_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='core.order'),
        ),
    ]