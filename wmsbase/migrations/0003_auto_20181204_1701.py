# Generated by Django 2.1.4 on 2018-12-04 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wmsbase', '0002_auto_20181204_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='type',
            field=models.ForeignKey(default=None, null=True, on_delete=models.SET('Тип юнита удален'), to='wmsbase.UnitType', verbose_name='Тип юнита'),
        ),
    ]
