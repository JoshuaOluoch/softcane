# Generated by Django 3.2.6 on 2021-08-09 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubLocation',
            fields=[
                ('tenantawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tenant.tenantawaremodel')),
                ('sub_location_id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(default='01', max_length=100, unique=True)),
                ('sub_location', models.CharField(max_length=255)),
            ],
            bases=('tenant.tenantawaremodel',),
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('tenantawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tenant.tenantawaremodel')),
                ('zones_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='01', max_length=1, unique=True)),
                ('lower_range', models.DecimalField(decimal_places=2, max_digits=100)),
                ('upper_range', models.DecimalField(decimal_places=2, max_digits=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=100)),
            ],
            bases=('tenant.tenantawaremodel',),
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('tenantawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tenant.tenantawaremodel')),
                ('field_id', models.AutoField(primary_key=True, serialize=False)),
                ('field_code', models.CharField(default='01', max_length=100, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('distance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sub_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.sublocation')),
            ],
            bases=('tenant.tenantawaremodel',),
        ),
    ]
