from django.db import models
from tenant.models import TenantAwareModel
from users.models import User
from django.utils.timezone import now
from accounting.models import TenantSupplier, TenantCustomer
from location.models import Branch


class StockCategory(TenantAwareModel):
    stock_category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=255, blank=True)
    examples = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description


class StockItem(TenantAwareModel):
    stock_item_id = models.AutoField(primary_key=True)
    item_code = models.CharField(max_length=20, blank=True)
    item_description = models.CharField(max_length=255, blank=True)
    item_part_number = models.CharField(max_length=255, blank=True)
    item_category = models.ForeignKey(StockCategory, on_delete=models.CASCADE)
    # item_location=models.CharField(max_length=50,blank=True)
    item_price = models.DecimalField(max_digits=1000, decimal_places=2)

    def __str__(self):
        return self.item_description


class FuelType(TenantAwareModel):
    fuel_type_id = models.AutoField(primary_key=True)
    fuel_type = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.fuel_type


class Tank(TenantAwareModel):
    tank_id = models.AutoField(primary_key=True)
    tank_code = models.CharField(max_length=255, blank=True)
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE)
    tank_capacity = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.tank_code


class FuelPump(TenantAwareModel):
    fuel_pump_id = models.AutoField(primary_key=True)
    fuel_pump_code = models.CharField(max_length=20, blank=True)
    fuel_pump_tank = models.OneToOneField(Tank, on_delete=models.CASCADE)
    fuel_branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.fuel_pump_code


class FuelReadings(TenantAwareModel):
    fuel_readings_id = models.AutoField(primary_key=True)
    date = models.DateField()
    fuel_pump = models.ForeignKey(FuelPump, on_delete=models.CASCADE)
    morning_tank_dipping = models.DecimalField(max_digits=100, decimal_places=2)
    morning_pump_reading = models.DecimalField(max_digits=100, decimal_places=2)
    evening_tank_dipping = models.DecimalField(max_digits=100, decimal_places=2)
    evening_pump_reading = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return 'Pump reading on:' + str(self.date) + ' Date:' + self.fuel_pump


class StockArticleReceipt(TenantAwareModel):
    receipt_id = models.AutoField(primary_key=True)
    date = models.DateField(default=now)
    internal_no = models.CharField(max_length=128, unique=True)
    reference_no = models.CharField(max_length=255, null=True, blank=True)
    supplier = models.ForeignKey(TenantSupplier, on_delete=models.CASCADE, null=True)
    remark = models.CharField(max_length=255, null=True, blank=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    posted_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.transaction_no

    #def save(self, *args, **kwargs):
        #print('Save model =>StockArticleReceipt')
     #   super(Model, self).save(*args, **kwargs)


class StockArticleReceiptItem(TenantAwareModel):
    stock_item_id = models.AutoField(primary_key=True, default=1)
    receipt_header_id = models.ForeignKey(StockArticleReceipt, on_delete=models.CASCADE)
    item = models.ForeignKey(StockItem, on_delete=models.CASCADE)
    quantity_received = models.IntegerField()
    unit_cost = models.DecimalField(max_digits=100, decimal_places=2)
    total_value = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return str(self.stock_item_id) + ' item:' + self.item.item_description


class StockArticleIssue(TenantAwareModel):
    stock_article_issue_id = models.AutoField(primary_key=True)
    transaction_no = models.CharField(max_length=128, unique=True)
    type = models.CharField(max_length=128, null=True, blank=True)
    date = models.DateField(default=now)
    reference_no = models.CharField(max_length=255, null=True, blank=True)
    customer = models.ForeignKey(TenantCustomer, on_delete=models.CASCADE)
    item = models.ForeignKey(StockItem, on_delete=models.CASCADE)
    item_category = models.ForeignKey(StockCategory, on_delete=models.CASCADE)
    part_number = models.CharField(max_length=128)
    quantity_received = models.IntegerField()
    unit_cost = models.DecimalField(max_digits=100, decimal_places=2)
    total_value = models.DecimalField(max_digits=100, decimal_places=2)
    remark = models.CharField(max_length=255, null=True, blank=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    posted_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.transaction_no


class StockArticleAdjustment(TenantAwareModel):
    stock_article_adjustment_id = models.AutoField(primary_key=True)
    transaction_no = models.CharField(max_length=128, unique=True)
    type = models.CharField(max_length=128, null=True, blank=True)
    date = models.DateField(default=now)
    reference_no = models.CharField(max_length=255, null=True, blank=True)
    item = models.ForeignKey(StockItem, on_delete=models.CASCADE)
    item_category = models.ForeignKey(StockCategory, on_delete=models.CASCADE)
    part_number = models.CharField(max_length=128)
    required_quantity = models.IntegerField()
    current_quantity = models.IntegerField()
    remark = models.CharField(max_length=255, null=True, blank=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    posted_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.transaction_no
