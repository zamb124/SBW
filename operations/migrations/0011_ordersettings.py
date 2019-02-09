# Generated by Django 2.1.4 on 2019-01-23 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0010_auto_20190122_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название настройки')),
                ('imgorder', models.ImageField(upload_to='', verbose_name='Image')),
            ],
        ),
    ]