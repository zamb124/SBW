# Generated by Django 2.1.4 on 2019-02-06 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0014_auto_20190206_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryhead',
            name='delivery_type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.DeliveryType', verbose_name='Тип поставки'),
        ),
    ]
