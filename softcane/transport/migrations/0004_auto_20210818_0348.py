# Generated by Django 3.1.5 on 2021-08-18 00:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tenant', '0002_auto_20210812_1200'),
        ('hr', '0006_auto_20210818_0348'),
        ('location', '0003_branch'),
        ('transport', '0003_auto_20210816_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceCompany',
            fields=[
                ('tenantawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tenant.tenantawaremodel')),
                ('insurance_company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
            bases=('tenant.tenantawaremodel',),
        ),
        migrations.CreateModel(
            name='InsuranceRisk',
            fields=[
                ('tenantawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tenant.tenantawaremodel')),
                ('insurance_risk_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            bases=('tenant.tenantawaremodel',),
        ),
        migrations.AlterField(
            model_name='transportinfo',
            name='transport_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('tenantawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tenant.tenantawaremodel')),
                ('trip_id', models.AutoField(primary_key=True, serialize=False)),
                ('trip_number', models.CharField(max_length=100)),
                ('ticket_number', models.CharField(max_length=100)),
                ('trip_date', models.DateField(default=django.utils.timezone.now)),
                ('field_in', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('field_out', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('time_in', models.TimeField(blank=True, null=True)),
                ('time_out', models.TimeField(blank=True, null=True)),
                ('weight_in', models.DecimalField(blank=True, decimal_places=3, max_digits=100, null=True)),
                ('weight_out', models.DecimalField(blank=True, decimal_places=3, max_digits=100, null=True)),
                ('net_weight', models.DecimalField(blank=True, decimal_places=3, max_digits=100, null=True)),
                ('trip_type', models.CharField(choices=[('FRESH', 'FRESH'), ('PARKED', 'PARKED'), ('TWICE', 'TWICE'), ('PREV UNTARED', 'PREV UNTARED')], default='FRESH', max_length=255)),
                ('posted_date', models.DateField(auto_now=True)),
                ('loaded_by_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tenant.vehicle')),
                ('loaded_by_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tenant.vehicle')),
                ('loading_driver_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='hr.employee')),
                ('loading_driver_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='hr.employee')),
                ('posted_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tractor_or_lorry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tenant.vehicle')),
                ('trip_branch', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='location.branch')),
                ('trip_driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='hr.employee')),
                ('trip_field', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='location.field')),
                ('trip_sub_location', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='location.sublocation')),
                ('trip_zone', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='location.zone')),
            ],
            bases=('tenant.tenantawaremodel',),
        ),
        migrations.CreateModel(
            name='TrailerAttachment',
            fields=[
                ('tenantawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tenant.tenantawaremodel')),
                ('trailer_attachment_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now=True)),
                ('posted_date', models.DateField(auto_now=True)),
                ('posted_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tenant.vehicle')),
                ('trailer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tenant.vehicle')),
            ],
            bases=('tenant.tenantawaremodel',),
        ),
        migrations.CreateModel(
            name='Towing',
            fields=[
                ('tenantawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tenant.tenantawaremodel')),
                ('towing_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today)),
                ('number_of_tows', models.IntegerField()),
                ('posted_date', models.DateField(auto_now=True)),
                ('branch_of_origin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.branch')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hr.employee')),
                ('posted_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('winch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tenant.vehicle')),
            ],
            bases=('tenant.tenantawaremodel',),
        ),
        migrations.CreateModel(
            name='TicketReconciliation',
            fields=[
                ('tenantawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tenant.tenantawaremodel')),
                ('ticket_reconciliation_id', models.AutoField(primary_key=True, serialize=False)),
                ('paid', models.BooleanField(default=False)),
                ('posted_date', models.DateField(auto_now=True)),
                ('posted_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ticket_trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.trip')),
            ],
            bases=('tenant.tenantawaremodel',),
        ),
        migrations.CreateModel(
            name='PickupsAndCantersControl',
            fields=[
                ('tenantawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tenant.tenantawaremodel')),
                ('pickup_canter_control_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today)),
                ('opening_reading', models.IntegerField()),
                ('closing_reading', models.IntegerField()),
                ('milage', models.DecimalField(decimal_places=2, max_digits=100)),
                ('posted_date', models.DateField(auto_now=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.employee')),
                ('posted_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenant.vehicle')),
            ],
            bases=('tenant.tenantawaremodel',),
        ),
        migrations.CreateModel(
            name='PackedCane',
            fields=[
                ('tenantawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tenant.tenantawaremodel')),
                ('packed_cane_id', models.AutoField(primary_key=True, serialize=False)),
                ('delivery_note', models.CharField(max_length=255, unique=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('stacks', models.IntegerField()),
                ('posted_date', models.DateField(auto_now=True)),
                ('Tractor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tenant.vehicle')),
                ('branch_of_origin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.branch')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='hr.employee')),
                ('loaded_by_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tenant.vehicle')),
                ('loaded_by_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tenant.vehicle')),
                ('loading_driver_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='hr.employee')),
                ('loading_driver_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='hr.employee')),
                ('posted_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('trip_field', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='location.field')),
                ('trip_sub_location', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='location.sublocation')),
                ('trip_zone', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='location.zone')),
            ],
            bases=('tenant.tenantawaremodel',),
        ),
        migrations.CreateModel(
            name='LoadersDailyEntry',
            fields=[
                ('tenantawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tenant.tenantawaremodel')),
                ('loaders_daily_entry', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today)),
                ('worked', models.BooleanField(default=True)),
                ('posted_date', models.DateField(auto_now=True)),
                ('loader_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.loader')),
                ('posted_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('tenant.tenantawaremodel',),
        ),
        migrations.CreateModel(
            name='InsuranceValidity',
            fields=[
                ('tenantawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tenant.tenantawaremodel')),
                ('insurance_validity_id', models.AutoField(primary_key=True, serialize=False)),
                ('certificate_number', models.CharField(max_length=255, unique=True)),
                ('policy_no', models.CharField(max_length=255, unique=True)),
                ('policy_type', models.CharField(choices=[('Third Party', 'Third Party'), ('Comprehensive', 'Comprehensive'), ('Other', 'Other')], default='Third Party', max_length=255)),
                ('commence_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('delivery_note_no', models.CharField(max_length=255)),
                ('insured_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.insurancecompany')),
                ('risk_covered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.insurancerisk')),
                ('vehicle_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenant.vehicle')),
            ],
            bases=('tenant.tenantawaremodel',),
        ),
        migrations.CreateModel(
            name='FuelConsumption',
            fields=[
                ('tenantawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tenant.tenantawaremodel')),
                ('fuel_consumption_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today)),
                ('quantity_in_litres', models.DecimalField(decimal_places=2, max_digits=100)),
                ('posted_date', models.DateField(auto_now=True)),
                ('branch_of_origin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.branch')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hr.employee')),
                ('posted_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle_fueled', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tenant.vehicle')),
            ],
            bases=('tenant.tenantawaremodel',),
        ),
        migrations.CreateModel(
            name='DrivingLicenceValidity',
            fields=[
                ('tenantawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tenant.tenantawaremodel')),
                ('licence_id', models.AutoField(primary_key=True, serialize=False)),
                ('active_driving_license', models.BooleanField(default=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.employee')),
            ],
            bases=('tenant.tenantawaremodel',),
        ),
    ]