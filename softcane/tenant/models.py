from django.db import models
#from location.models import Branch

class Tenant(models.Model):
    tenant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    subdomain= models.CharField(max_length=255)
    created_on = models.DateField(auto_now=True)
    postal_code = models.CharField(max_length=255, null=True)
    telephone = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)
    pin_number = models.CharField(max_length=255, null=True)
    vat_number = models.CharField(max_length=255, null=True)
    payroll_date = models.DateField(null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

class VehicleType(TenantAwareModel):
    vehicle_type_id = models.AutoField(primary_key = True)
    type = models.CharField(max_length=2)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class Vehicle(TenantAwareModel):
    vehicle_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, unique=True)
    registration = models.CharField(max_length=255)
    make = models.CharField(max_length=255, blank=True)
    engine_no = models.CharField(max_length=255,null=True, blank=True)
    chassis_no = models.CharField(max_length=255,null=True, blank=True)
    vehicle_model = models.CharField(max_length=255, blank=True)
    date_of_manufacture = models.DateField(null=True, blank=True)
    body_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE, blank=True,related_name='+')
    body_color = models.CharField(max_length=128,blank=True)
    lts_per_kms = models.DecimalField(decimal_places = 10, max_digits = 300)

    def __str__(self):
        return self.registration









