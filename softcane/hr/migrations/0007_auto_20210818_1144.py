# Generated by Django 3.1.5 on 2021-08-18 08:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0006_auto_20210818_0348'),
    ]

    operations = [
        migrations.AddField(
            model_name='nhifband',
            name='effective_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payeband',
            name='created_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='loader',
            name='date_registered',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
