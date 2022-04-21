# Generated by Django 4.0.4 on 2022-04-21 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0008_alter_vatcodeslisting_vat_code'),
        ('tenant', '0005_alter_tenantawaremodel_id'),
        ('stock', '0007_fuelreadings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockarticlereceipt',
            old_name='transaction_no',
            new_name='internal_no',
        ),
        migrations.RenameField(
            model_name='stockarticlereceipt',
            old_name='stock_article_receipt_id',
            new_name='receipt_id',
        ),
        migrations.RemoveField(
            model_name='stockarticlereceipt',
            name='item',
        ),
        migrations.RemoveField(
            model_name='stockarticlereceipt',
            name='item_category',
        ),
        migrations.RemoveField(
            model_name='stockarticlereceipt',
            name='part_number',
        ),
        migrations.RemoveField(
            model_name='stockarticlereceipt',
            name='quantity_received',
        ),
        migrations.RemoveField(
            model_name='stockarticlereceipt',
            name='supplier_account',
        ),
        migrations.RemoveField(
            model_name='stockarticlereceipt',
            name='total_value',
        ),
        migrations.RemoveField(
            model_name='stockarticlereceipt',
            name='type',
        ),
        migrations.RemoveField(
            model_name='stockarticlereceipt',
            name='unit_cost',
        ),
        migrations.AddField(
            model_name='stockarticlereceipt',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.tenantsupplier'),
        ),
        migrations.CreateModel(
            name='StockArticleReceiptItem',
            fields=[
                ('tenantawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tenant.tenantawaremodel')),
                ('stock_item_id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('quantity_received', models.IntegerField()),
                ('unit_cost', models.DecimalField(decimal_places=2, max_digits=100)),
                ('total_value', models.DecimalField(decimal_places=2, max_digits=100)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.stockitem')),
                ('receipt_header_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.stockarticlereceipt')),
            ],
            bases=('tenant.tenantawaremodel',),
        ),
    ]