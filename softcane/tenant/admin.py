from django.contrib import admin
from .models import Tenant, VehicleType, Vehicle

admin.site.register(Tenant)
admin.site.register(VehicleType)
admin.site.register(Vehicle)