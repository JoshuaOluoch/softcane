# Generated by Django 4.0.4 on 2022-04-21 11:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0005_alter_tenantawaremodel_id'),
        ('hr', '0007_auto_20210818_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='employee_contact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_next_of_kin',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_next_of_kin_contact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_nhif_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_nssf_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_union',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='HolidayPay',
            fields=[
                ('tenantawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tenant.tenantawaremodel')),
                ('holidaypay_id', models.AutoField(primary_key=True, serialize=False)),
                ('trans_code', models.CharField(blank=True, max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.employee')),
            ],
            bases=('tenant.tenantawaremodel',),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('tenantawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tenant.tenantawaremodel')),
                ('attendance_id', models.AutoField(primary_key=True, serialize=False)),
                ('attend', models.CharField(choices=[('ABSENT', 'ABSENT'), ('PRESENT', 'PRESENT'), ('ABSENT WITH PERMISSION', 'ABSENT WITH PERMISSION')], default='Absent', max_length=255)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('department_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.department')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.employee')),
            ],
            bases=('tenant.tenantawaremodel',),
        ),
        migrations.CreateModel(
            name='AllowanceAndDeductions',
            fields=[
                ('tenantawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tenant.tenantawaremodel')),
                ('allowance_id', models.AutoField(primary_key=True, serialize=False)),
                ('trans_code', models.CharField(blank=True, max_length=10)),
                ('desc', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.employee')),
            ],
            bases=('tenant.tenantawaremodel',),
        ),
    ]