# Generated by Django 2.1.4 on 2018-12-04 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wmsbase', '0007_warehouseobject_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouseobject',
            name='ident',
            field=models.CharField(max_length=20, null=True, verbose_name='Идентификатор'),
        ),
    ]
