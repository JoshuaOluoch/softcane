# Generated by Django 3.1.5 on 2021-08-23 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0002_auto_20210812_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='chassis_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='date_of_manufacture',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='engine_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='lts_per_kms',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=300),
            preserve_default=False,
        ),
    ]
