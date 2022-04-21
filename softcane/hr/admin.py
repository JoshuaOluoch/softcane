from django.contrib import admin
from .models import Designation, Department, Employee, TransportPayrollRate, PayrollCode, PayeBand, NhifBand, Attendance, AllowanceAndDeductions, HolidayPay

admin.site.register(Designation)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(TransportPayrollRate)
admin.site.register(PayrollCode)
admin.site.register(PayeBand)
admin.site.register(NhifBand)
admin.site.register(Attendance)
admin.site.register(AllowanceAndDeductions)
admin.site.register(HolidayPay)
