# Generated by Django 2.1.4 on 2019-02-02 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='url',
            field=models.CharField(blank=True, default='0', max_length=100, null=True, verbose_name='Количество операций'),
        ),
    ]
