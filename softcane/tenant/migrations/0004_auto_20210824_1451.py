# Generated by Django 3.1.5 on 2021-08-24 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0003_auto_20210823_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='body_type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tenant.vehicletype'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='registration',
            field=models.CharField(max_length=255),
        ),
    ]