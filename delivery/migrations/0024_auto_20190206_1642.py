# Generated by Django 2.1.4 on 2019-02-06 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0023_auto_20190206_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryposition',
            name='delivery_position_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.DeliveryPositionType', verbose_name='Тип позиции поставки'),
        ),
        migrations.AlterField(
            model_name='deliverypositiontype',
            name='erp_link',
            field=models.CharField(blank=True, help_text='Ссылка на тип позиции поставки в ERP истемах, можно использовать как имя сервиса', max_length=40, null=True, verbose_name='Тип позиции поставки ERP'),
        ),
    ]
