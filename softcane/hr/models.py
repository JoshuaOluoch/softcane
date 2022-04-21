from django.db import models
from tenant.models import TenantAwareModel
from django.utils.timezone import now
from django.utils import timezone

GENDER = [
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
]
ATTENDANCE = [
    ('ABSENT', 'ABSENT'),
    ('PRESENT', 'PRESENT'),
    ('ABSENT WITH PERMISSION', 'ABSENT WITH PERMISSION'),
]


class Designation(TenantAwareModel):
    designation_id = models.AutoField(primary_key=True)
    designation_code = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description


class Department(TenantAwareModel):
    department_id = models.AutoField(primary_key=True)
    department_category = models.CharField(max_length=255, blank=True)
    department_description = models.CharField(max_length=255, blank=True)
    department_narration = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.department_description


DEFAULT_DESIGNATION_ID = 1
DEFAULT_DEPARTMENT_ID = 1


class Employee(TenantAwareModel):
    employee_id = models.AutoField(primary_key=True)
    employee_code = models.CharField(max_length=255, blank=True)
    employee_first_name = models.CharField(max_length=255, blank=True)
    employee_last_name = models.CharField(max_length=255, blank=True)
    employee_designation = models.ForeignKey(Designation, on_delete=models.CASCADE, default=DEFAULT_DESIGNATION_ID)
    employee_department = models.ForeignKey(Department, on_delete=models.CASCADE, default=DEFAULT_DEPARTMENT_ID)
    employee_id_number = models.CharField(max_length=255, blank=True)
    employee_kra_pin = models.CharField(max_length=255, blank=True)
    employee_nhif_no = models.CharField(max_length=100, blank=True, null=True)
    employee_nssf_no = models.CharField(max_length=100, blank=True, null=True)
    employee_union = models.CharField(max_length=255, blank=True, null=True)
    employee_contact = models.CharField(max_length=255, blank=True, null=True)
    employee_next_of_kin = models.CharField(max_length=255, blank=True, null=True)
    employee_next_of_kin_contact = models.CharField(max_length=255, blank=True, null=True)
    employee_sex = models.CharField(choices=GENDER, max_length=255, default='MALE')
    employee_address = models.CharField(max_length=255, blank=True)
    employee_account_number = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.employee_first_name + " " + self.employee_last_name


class TransportPayrollRate(TenantAwareModel):
    transport_pay_roll_rate_id = models.AutoField(primary_key=True)
    single_bundle = models.DecimalField(max_digits=20, decimal_places=2)
    double_bundle = models.DecimalField(max_digits=20, decimal_places=2)
    weighing_clerk_bundle = models.DecimalField(max_digits=20, decimal_places=2)
    field_clerk_bundle = models.DecimalField(max_digits=20, decimal_places=2)
    cameco_operator = models.DecimalField(max_digits=20, decimal_places=2)
    bell_operator = models.DecimalField(max_digits=20, decimal_places=2)
    winch_operator = models.DecimalField(max_digits=20, decimal_places=2)
    loader_rate = models.DecimalField(max_digits=20, decimal_places=2)
    created_date = models.DateField(auto_now=True)


class PayrollCode(TenantAwareModel):
    payroll_code_id = models.AutoField(primary_key=True)
    payroll_code = models.CharField(max_length=20, blank=True)
    payroll_description = models.CharField(max_length=255, blank=True)
    payroll_usage = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.payroll_description


class PayeBand(TenantAwareModel):
    paye_band_id = models.AutoField(primary_key=True)
    paye_band_tax = models.DecimalField(decimal_places=2, max_digits=20)
    paye_band_description = models.CharField(max_length=255, blank=True)
    paye_band_lower_range = models.DecimalField(decimal_places=2, max_digits=20)
    paye_band_upper_range = models.DecimalField(decimal_places=2, max_digits=20)
    paye_band_amount = models.DecimalField(decimal_places=2, max_digits=20)
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.paye_band_description


class NhifBand(TenantAwareModel):
    nhif_band_id = models.AutoField(primary_key=True)
    nhif_band_description = models.CharField(max_length=255, blank=True)
    nhif_band_lower_range = models.DecimalField(decimal_places=2, max_digits=20)
    nhif_band_upper_range = models.DecimalField(decimal_places=2, max_digits=20)
    nhif_band_amount = models.DecimalField(decimal_places=2, max_digits=20)
    effective_date = models.DateField()

    def __str__(self):
        return self.nhif_band_description


class Loader(TenantAwareModel):
    loaders_id = models.AutoField(primary_key=True)
    name = models.OneToOneField(Employee, on_delete=models.CASCADE, unique=True)
    date_registered = models.DateField(default=now)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name.employee_first_name + ' ' + self.name.employee_last_name


class Attendance(TenantAwareModel):
    attendance_id = models.AutoField(primary_key=True)
    name = models.ForeignKey(Employee, on_delete=models.CASCADE, )
    department_category = models.ForeignKey(Department, on_delete=models.CASCADE)
    attend = models.CharField(choices=ATTENDANCE, max_length=255, default='Absent')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name.employee_first_name + " " + self.name.employee_last_name


class AllowanceAndDeductions(TenantAwareModel):
    allowance_id = models.AutoField(primary_key=True)
    name = models.ForeignKey(Employee, on_delete=models.CASCADE, )
    trans_code = models.CharField(max_length=10, blank=True)
    desc = models.CharField(max_length=50, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name.employee_first_name + " " + self.name.employee_last_name


class HolidayPay(TenantAwareModel):
    holidaypay_id = models.AutoField(primary_key=True)
    name = models.ForeignKey(Employee, on_delete=models.CASCADE, )
    trans_code = models.CharField(max_length=10, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name.employee_first_name + " " + self.name.employee_last_name
