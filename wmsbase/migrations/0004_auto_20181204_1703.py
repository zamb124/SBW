# Generated by Django 2.1.4 on 2018-12-04 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wmsbase', '0003_auto_20181204_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='type',
        ),
    ]
