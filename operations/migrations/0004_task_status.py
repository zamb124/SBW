# Generated by Django 2.1.4 on 2018-12-13 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0003_auto_20181211_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('b', 'Blank'), ('n', 'New)'), ('p', 'In progress'), ('d', 'Done')], default='Blank', max_length=20, verbose_name='Статус'),
        ),
    ]