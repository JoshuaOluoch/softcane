# Generated by Django 3.1.5 on 2021-08-12 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_accountsgroupinglisting_main_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountsgroupinglisting',
            name='main_group',
        ),
        migrations.AlterField(
            model_name='accountsgroupinglisting',
            name='classification',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounting.accountsheadingslisting'),
        ),
    ]
