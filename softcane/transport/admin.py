from django.contrib import admin
from .models import (TransportInfo, Trip, FuelConsumption, Towing, PackedCane, LoadersDailyEntry,
                     PickupsAndCantersControl, TicketReconciliation, TrailerAttachment, InsuranceRisk, InsuranceCompany,
                     InsuranceValidity, DrivingLicenceValidity)

admin.site.register(TransportInfo)
admin.site.register(Trip)
admin.site.register(FuelConsumption)
admin.site.register(Towing)
admin.site.register(PackedCane)
admin.site.register(LoadersDailyEntry)
admin.site.register(PickupsAndCantersControl)
admin.site.register(TicketReconciliation)
admin.site.register(TrailerAttachment)
admin.site.register(InsuranceRisk)
admin.site.register(InsuranceCompany)
admin.site.register(InsuranceValidity)
admin.site.register(DrivingLicenceValidity)
