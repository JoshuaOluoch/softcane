# Generated by Django 3.1.5 on 2021-08-20 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0005_auto_20210819_1551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loadersdailyentry',
            old_name='loaders_daily_entry',
            new_name='loaders_daily_entry_id',
        ),
    ]