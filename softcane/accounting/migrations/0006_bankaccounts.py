# Generated by Django 3.1.5 on 2021-08-18 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0002_auto_20210812_1200'),
        ('accounting', '0005_auto_20210813_0607'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccounts',
            fields=[
                ('tenantawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tenant.tenantawaremodel')),
                ('bank_account_id', models.AutoField(primary_key=True, serialize=False)),
                ('bank_account', models.CharField(max_length=255, unique=True)),
                ('bank_account_description', models.CharField(max_length=255, unique=True)),
                ('bank_name', models.CharField(choices=[('Petty Cash', 'Petty Cash'), ('ABC Bank(Kenya)', 'ABC Bank(Kenya)'), ('Absa Bank Kenya', 'Absa Bank Kenya'), ('Access Bank Kenya', 'Access Bank Kenya'), ('Bank of Africa', 'Bank of Africa'), ('Bank of Baroda', 'Bank of Baroda'), ('Bank of India', 'Bank of India'), ('Citibank', 'Citibank'), ('Consolidated Bank of Kenya', 'Consolidated Bank of Kenya'), ('Cooperative Bank of Kenya', 'Cooperative Bank of Kenya'), ('Credit Bank', 'Credit Bank'), ('Development Bank of Kenya', 'Development Bank of Kenya'), ('Diamond Trust Bank', 'Development Bank of Kenya'), ('Dubai Islamic Bank', 'Dubai Islamic Bank'), ('Ecobank Kenya', 'Ecobank Kenya'), ('Equity Bank Kenya', 'Equity Bank Kenya'), ('Family Bank', 'Family Bank'), ('First Community Bank', 'First Community Bank'), ('Guaranty Trust Bank Kenya', 'Guaranty Trust Bank Kenya'), ('Guardian Bank', 'Guardian Bank'), ('Gulf African Bank', 'Gulf African Bank'), ('Habib Bank AG Zurich', 'Habib Bank AG Zurich'), ('Housing Finance Company of Kenya', 'Housing Finance Company of Kenya'), ('I & M Bank', 'I & M Bank'), ('Imperial Bank Kenya(In receivership)', 'Imperial Bank Kenya(In receivership)'), ('Kingdom Bank Limited Kenya', 'Kingdom Bank Limited Kenya'), ('Commercial Bank', 'Commercial Bank'), ('Mayfair Bank', 'Mayfair Bank'), ('Middle East Bank Kenya', 'Middle East Bank Kenya'), ('M Oriental Bank', 'M Oriental Bank'), ('National Bank of Kenya', 'National Bank of Kenya'), ('NCBA Bank Kenya', 'NCBA Bank Kenya'), ('Paramount Universal Bank', 'Paramount Universal Bank'), ('Prime Bank(Kenya)', 'Prime Bank(Kenya)'), ('SBM Bank Kenya', 'SBM Bank Kenya'), ('Sidian Bank', 'Sidian Bank'), ('Spire Bank', 'Spire Bank'), ('Stanbic Holdings Plc', 'Stanbic Holdings Plc'), ('Standard Chartered Kenya', 'Standard Chartered Kenya'), ('United Bank for Africa', 'United Bank for Africa'), ('Victoria Commercial Bank', 'Victoria Commercial Bank'), ('HDFC Bank', 'HDFC Bank'), ('Nedbank', 'Nedbank'), ('FirstRand Bank', 'FirstRand Bank'), ('Bank of China', 'Bank of China'), ('JP Morgan Chase', 'JP Morgan Chase'), ('Bank of Kigali', 'Bank of Kigali'), ('Bank AL Habib', 'Bank AL Habib')], default='Bank of Baroda', max_length=255)),
            ],
            bases=('tenant.tenantawaremodel',),
        ),
    ]
