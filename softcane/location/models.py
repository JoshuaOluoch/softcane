from django.db import models
from tenant.models import TenantAwareModel


class Branch(TenantAwareModel):
    branch_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, null = True, blank = True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Zone(TenantAwareModel):
    zones_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=1, unique=True, default="01")
    lower_range = models.DecimalField(max_digits=100, decimal_places=2)
    upper_range = models.DecimalField(max_digits=100, decimal_places=2)
    amount = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.name

class SubLocation(TenantAwareModel):
    sub_location_id = models.AutoField(primary_key = True)
    code = models.CharField(max_length=100, unique=True)
    sub_location = models.CharField(max_length=255 )

    def __str__(self):
        return self.sub_location

class Field(TenantAwareModel):
    field_id = models.AutoField(primary_key=True)
    field_code = models.CharField(max_length=100, unique=False)
    name = models.CharField(max_length=255)
    sub_location = models.ForeignKey(SubLocation,on_delete=models.CASCADE)
    distance=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name


