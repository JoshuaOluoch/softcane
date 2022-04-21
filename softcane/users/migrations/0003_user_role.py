# Generated by Django 3.2.6 on 2021-09-06 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_tenant'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('admin', 'Admin'), ('clerk', 'Clerk'), ('accountant', 'Accountant'), ('driver', 'Driver')], max_length=20, null=True),
        ),
    ]
