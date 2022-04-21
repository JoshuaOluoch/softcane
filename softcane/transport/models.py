from django.db import models
from tenant.models import TenantAwareModel, Vehicle
from location.models import Branch, Zone, SubLocation, Field
import datetime
from hr.models import Employee, Loader
from users.models import User
from django.utils.timezone import now

DAY_CONDITION_CHOICES = [
    ('DRY', 'DRY'),
    ('WET', 'WET'),
    ('VERY WET', 'VERY WET'),
]

DAY_DIRECTION_CHOICES = [
    ('NORTH', 'NORTH'),
    ('SOUTH', 'SOUTH'),
    ('WEST', 'WEST'),
    ('EAST', 'EAST'),
]

DAY_STATUS_CHOICES = [
    ('NORMAL', 'NORMAL'),
    ('HOLIDAY', 'HOLIDAY'),
    ('PPM', 'PPM'),
    ('OOC', 'OOC'),
]


class TransportInfo(TenantAwareModel):
    transport_info_id = models.AutoField(primary_key=True)
    transport_date = models.DateField(default=now)
    field_clerk_1 = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='+')
    field_clerk_2 = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='+')
    weighbridge_clerk_1 = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='+')
    weighbridge_clerk_2 = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='+')
    inter_field_movement = models.IntegerField()
    target_tons = models.DecimalField(max_digits=20, decimal_places=2)
    actual_tons = models.DecimalField(max_digits=20, decimal_places=2)
    day_condition = models.CharField(max_length=255, choices=DAY_CONDITION_CHOICES, default='DRY')
    day_direction = models.CharField(max_length=255, choices=DAY_DIRECTION_CHOICES, default='NORTH')
    day_status = models.CharField(max_length=255, choices=DAY_STATUS_CHOICES, default='NORMAL')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    posted_date = models.DateField(auto_now=True)

    def __str__(self):
        return 'Transport information for: ' + str(self.date)


class Trip(TenantAwareModel):
    trip_id = models.AutoField(primary_key=True)
    trip_number = models.CharField(max_length=100)
    ticket_number = models.CharField(max_length=100)
    trip_branch = models.ForeignKey(Branch, on_delete=models.CASCADE, default=1, blank=True)
    trip_zone = models.ForeignKey(Zone, on_delete=models.CASCADE, blank=True)
    trip_sub_location = models.ForeignKey(SubLocation, on_delete=models.CASCADE, blank=True)
    trip_field = models.ForeignKey(Field, on_delete=models.CASCADE, blank=True)
    trip_date = models.DateField(default=now)
    tractor_or_lorry = models.ForeignKey(Vehicle, on_delete=models.CASCADE, blank=True, related_name='+', null=True)
    trip_driver = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    field_in = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    field_out = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    field_net = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    loaded_by_1 = models.ForeignKey(Vehicle, on_delete=models.CASCADE, blank=True, related_name='+', null=True)
    loading_driver_1 = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    loaded_by_2 = models.ForeignKey(Vehicle, on_delete=models.CASCADE, blank=True, related_name='+', null=True)
    loading_driver_2 = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    time_in = models.TimeField(null=True, blank=True)
    time_out = models.TimeField(null=True, blank=True)
    weight_in = models.DecimalField(max_digits=100, decimal_places=3, null=True, blank=True)
    weight_out = models.DecimalField(max_digits=100, decimal_places=3, null=True, blank=True)
    net_weight = models.DecimalField(max_digits=100, decimal_places=3, null=True, blank=True)
    trip_type = models.CharField(max_length=255, choices=[('FRESH', 'FRESH'), ('PARKED', 'PARKED'), ('TWICE', 'TWICE'),
                                                          ('PREV UNTARED', 'PREV UNTARED'), ], default='FRESH')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    posted_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.trip_number


class FuelConsumption(TenantAwareModel):
    fuel_consumption_id = models.AutoField(primary_key=True)
    date = models.DateField(default=datetime.date.today)
    vehicle_fueled = models.ForeignKey(Vehicle, on_delete=models.CASCADE, blank=True, null=True)
    branch_of_origin = models.ForeignKey(Branch, on_delete=models.CASCADE, blank=True, null=True)
    driver = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    quantity_in_litres = models.DecimalField(max_digits=100, decimal_places=2)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    posted_date = models.DateField(auto_now=True)

    def __str__(self):
        return 'Fuel for Vehicle:' + self.vehicle + ' on date:' + str(self.date)


class Towing(TenantAwareModel):
    towing_id = models.AutoField(primary_key=True)
    date = models.DateField(default=datetime.date.today)
    winch = models.ForeignKey(Vehicle, on_delete=models.CASCADE, blank=True, null=True)
    branch_of_origin = models.ForeignKey(Branch, on_delete=models.CASCADE, blank=True, null=True)
    driver = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    number_of_tows = models.IntegerField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    posted_date = models.DateField(auto_now=True)

    def __str__(self):
        return 'Towing for winch:' + self.winch + ' on date:' + str(self.date)


class PackedCane(TenantAwareModel):
    packed_cane_id = models.AutoField(primary_key=True)
    delivery_note = models.CharField(max_length=255, unique=True)
    date = models.DateField(default=datetime.date.today)
    branch_of_origin = models.ForeignKey(Branch, on_delete=models.CASCADE, blank=True, null=True)
    trip_zone = models.ForeignKey(Zone, on_delete=models.CASCADE, blank=True)
    trip_sub_location = models.ForeignKey(SubLocation, on_delete=models.CASCADE, blank=True)
    trip_field = models.ForeignKey(Field, on_delete=models.CASCADE, blank=True)
    tractor = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    driver = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    loaded_by_1 = models.ForeignKey(Vehicle, on_delete=models.CASCADE, blank=True, related_name='+', null=True)
    loading_driver_1 = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    loaded_by_2 = models.ForeignKey(Vehicle, on_delete=models.CASCADE, blank=True, related_name='+', null=True)
    loading_driver_2 = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    stacks = models.IntegerField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    posted_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.delivery_note


class LoadersDailyEntry(TenantAwareModel):
    loaders_daily_entry_id = models.AutoField(primary_key=True)
    date = models.DateField(default=datetime.date.today)
    loader_name = models.ForeignKey(Loader, on_delete=models.CASCADE)
    worked = models.BooleanField(default=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    posted_date = models.DateField(auto_now=True)

    def __str__(self):
        return 'Loader Entry for:' + self.loader.loaders.employee_first_name + ' ' + self.loader.loaders.employee_last_name + ' on ' + str(
            self.date)


class PickupsAndCantersControl(TenantAwareModel):
    pickup_canter_control_id = models.AutoField(primary_key=True)
    date = models.DateField(default=datetime.date.today)
    vehicle_name = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Employee, on_delete=models.CASCADE)
    opening_reading = models.IntegerField()
    closing_reading = models.IntegerField()
    milage = models.DecimalField(max_digits=100, decimal_places=2)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    posted_date = models.DateField(auto_now=True)


class TicketReconciliation(TenantAwareModel):
    ticket_reconciliation_id = models.AutoField(primary_key=True)
    ticket_trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    posted_date = models.DateField(auto_now=True)


class TrailerAttachment(TenantAwareModel):
    trailer_attachment_id = models.AutoField(primary_key=True)
    tractor = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='+')
    trailer = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='+')
    date = models.DateField(auto_now=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    posted_date = models.DateField(auto_now=True)

    def __str__(self):
        return 'Tractor: ' + self.tractor.registration + ', Trailer: ' + self.trailer.registration


class InsuranceRisk(TenantAwareModel):
    insurance_risk_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class InsuranceCompany(TenantAwareModel):
    insurance_company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class InsuranceValidity(TenantAwareModel):
    insurance_validity_id = models.AutoField(primary_key=True)
    certificate_number = models.CharField(max_length=255, unique=True)
    vehicle_name = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    policy_no = models.CharField(max_length=255, unique=True)
    policy_type = models.CharField(max_length=255,
                                   choices=[('Third Party', 'Third Party'), ('Comprehensive', 'Comprehensive'),
                                            ('Other', 'Other')], default='Third Party')
    commence_date = models.DateField()
    expiry_date = models.DateField()
    delivery_note_no = models.CharField(max_length=255)
    risk_covered = models.ForeignKey(InsuranceRisk, on_delete=models.CASCADE)
    insured_by = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE)

    def __str__(self):
        return self.vehicle + ' :' + self.certificate_number


class DrivingLicenceValidity(TenantAwareModel):
    licence_id = models.AutoField(primary_key=True)
    driver = models.ForeignKey(Employee, on_delete=models.CASCADE)
    active_date = models.DateField(default=now)
    expiry_date = models.DateField(default=now)
    licence_no = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.driver.employee_first_name + self.driver.employee_last_name + ': ' + self.licence_no
