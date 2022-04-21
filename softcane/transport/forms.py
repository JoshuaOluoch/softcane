from .models import (TransportInfo, Trip, FuelConsumption, Towing, PackedCane, LoadersDailyEntry,
                     PickupsAndCantersControl,
                     TicketReconciliation, TrailerAttachment, InsuranceRisk, InsuranceCompany, InsuranceValidity,
                     DrivingLicenceValidity)

from django.db.models.functions import Concat
from hr.models import Employee, Loader
from location.models import Branch, Zone, SubLocation, Field
from tenant.models import TenantAwareModel, Vehicle
from users.models import User
from django import forms
from django.db.models import Q
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import Div
from crispy_forms import bootstrap, layout
from django.urls import reverse
from crispy_forms.layout import Layout, Submit


class DateInput(forms.DateInput):
    input_type = 'date'
    format = "%Y-%m-%d"


class TransportInfoForm(forms.ModelForm):
    transport_date = forms.DateField(label='Date', widget=DateInput())
    field_clerk_1 = forms.ModelChoiceField(label='Field Clerk 1', queryset=Employee.objects.filter(
        employee_designation__designation_code='008').order_by('employee_first_name'))
    field_clerk_2 = forms.ModelChoiceField(label='Field Clerk 2', queryset=Employee.objects.filter(
        employee_designation__designation_code='008').order_by('employee_first_name'), required=False)
    weighbridge_clerk_1 = forms.ModelChoiceField(label='Weighbridge Clerk 1', queryset=Employee.objects.filter(
        employee_designation__designation_code='009').order_by('employee_first_name'))
    weighbridge_clerk_2 = forms.ModelChoiceField(label='Weighbridge Clerk 2', queryset=Employee.objects.filter(
        employee_designation__designation_code='009').order_by('employee_first_name'), required=False)
    inter_field_movement = forms.IntegerField(label='inter_field_movement', min_value=0)
    target_tons = forms.DecimalField(min_value=0)
    actual_tons = forms.DecimalField(min_value=0)

    def __init__(self, *args, **kwargs):
        super(TransportInfoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('transport_date', css_class="col-sm-3"),
                    Div('field_clerk_1', css_class="col-sm-3"),
                    Div('field_clerk_2', css_class="col-sm-3"),
                    Div('weighbridge_clerk_1', css_class="col-sm-3"),
                    css_class='row'
                ),
                Div(
                    Div('weighbridge_clerk_2', css_class="col-sm-3"),
                    Div('inter_field_movement', css_class="col-sm-3"),
                    Div('target_tons', css_class="col-sm-3"),
                    Div('actual_tons', css_class="col-sm-3"),
                    css_class='row'
                ),
                Div(
                    Div('day_condition', css_class="col-sm-3"),
                    Div('day_direction', css_class="col-sm-3"),
                    Div('day_status', css_class="col-sm-3"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("transport_info")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),

                css_class='container'
            )

        )

    class Meta:
        model = TransportInfo
        fields = ['transport_date', 'field_clerk_1', 'field_clerk_2', 'weighbridge_clerk_1',
                  'weighbridge_clerk_2', 'inter_field_movement', 'target_tons', 'actual_tons',
                  'day_condition', 'day_direction', 'day_status']
        widgets = {
            'transport_date': DateInput(),
        }


class TripForm(forms.ModelForm):
    trip_branch = forms.ModelChoiceField(label='Branch', queryset=Branch.objects.all().order_by('name'),
                                         required=True, )
    trip_number = forms.CharField(label='Trip No.', required=True, max_length=80, )
    ticket_number = forms.CharField(label='Ticket No.', required=True, max_length=80, )
    trip_zone = forms.ModelChoiceField(label='Zone', queryset=Zone.objects.all().order_by('name'), required=False, )
    trip_sub_location = forms.ModelChoiceField(label='Sub Location',
                                               queryset=SubLocation.objects.all().order_by('sub_location'),
                                               required=False, )
    trip_field = forms.ModelChoiceField(label='Field', queryset=Field.objects.all().order_by('name'), required=False, )
    trip_date = forms.DateField(label='Date:', widget=DateInput(), )
    tractor_or_lorry = forms.ModelChoiceField(label='Tractor/Lorry', queryset=Vehicle.objects.filter(
        Q(body_type__type='LR') | Q(body_type__type='TR')).order_by('registration'))
    trip_driver = forms.ModelChoiceField(label='Driver', queryset=Employee.objects.filter(
        Q(employee_designation__designation_code='004') | Q(employee_designation__designation_code='006') | Q(
            employee_designation__designation_code='035')).order_by('employee_first_name'))
    loaded_by_1 = forms.ModelChoiceField(label='Loaded by 1', queryset=Vehicle.objects.filter(
        Q(body_type__type='CM') | Q(body_type__type='BL')).order_by('registration'), required=True)
    loaded_by_2 = forms.ModelChoiceField(label='Loaded by 2', queryset=Vehicle.objects.filter(
        Q(body_type__type='CM') | Q(body_type__type='BL')).order_by('registration'), required=False, )
    loading_driver_1 = forms.ModelChoiceField(label='Loading Driver 1', queryset=Employee.objects.filter(
        employee_designation__designation_code='005').order_by(
        'employee_first_name'),
                                              required=True,
                                              )
    loading_driver_2 = forms.ModelChoiceField(label='Loading Driver 2', queryset=Employee.objects.filter(
        employee_designation__designation_code='005').order_by(
        'employee_first_name'),
                                              required=False,
                                              )
    field_in = forms.DecimalField(label="Weight In", required=False)
    field_out = forms.DecimalField(label="Weight Out", required=False)

    def __init__(self, *args, **kwargs):
        super(TripForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_method = 'POST'
        self.helper.form_id = 'id-tripForm'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div(
                        Div(
                            Div(layout.HTML(f'<h5>Transport Info</h5'), css_class="row"),
                            Div(
                                Div('trip_branch', css_class="col-sm-3"),
                                Div('trip_number', css_class="col-sm-4"),
                                Div('ticket_number', css_class="col-sm-4"),
                                css_class='row'
                            ),
                            Div(
                                Div('trip_zone', css_class="col-sm-3"),
                                Div('trip_sub_location', css_class="col-sm-5"),
                                Div('trip_field', css_class="col-sm-3"),
                                css_class='row'
                            ),
                            Div(
                                Div('trip_date', css_class="col-sm-4"),
                                Div('tractor_or_lorry', css_class="col-sm-5"),
                                Div('trip_driver', css_class="col-sm-3"),
                                css_class="row"
                            ),

                            Div(
                                Div('loaded_by_1', css_class="col-sm-5"),
                                Div('loading_driver_1', css_class="col-sm-6"),
                                css_class='row'
                            ),
                            Div(
                                Div('loaded_by_2', css_class="col-sm-5"),
                                Div('loading_driver_2', css_class="col-sm-6"),
                                css_class='row'
                            ),
                            Div(
                                Div('trip_type', css_class="col-sm-4"),
                                css_class="row"),
                            css_class="card-body"),
                        css_class="card"),

                    css_class="row"),
                Div(Div(
                    Div(
                        Div(layout.HTML(f'<h5 class="card-title">Field Info</h5')),
                        Div(
                            Div('field_in', css_class="col-sm-4"),
                            Div('field_out', css_class="col-sm-4"),
                            css_class="row"),
                        css_class="card-body"
                    ),
                    css_class="card"),
                    css_class="row"),
                Div(
                    Div(
                        Div(
                            Div(layout.HTML(f'<h5 class="card-title">Factory Info</h5')),
                            Div(
                                Div('weight_in', css_class="col-sm-4"),
                                Div('weight_out', css_class="col-sm-4"),
                                Div(layout.HTML(
                                    f'<label for="result">Net Weight:</label> <input type="number" step="0.001" class="numberinput form-control" disabled="disabled" name="result" id="result" >'),
                                    css_class="col-sm-4"),
                                bootstrap.FormActions(
                                    layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                                    layout.HTML(
                                        f'<a href="{reverse("trip")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                                ),
                                css_class="row"),
                            css_class="card-body"
                        ),
                        css_class="card"
                    ),

                    css_class="row"),
                css_class='container-fluid'
            )

        )

    class Meta:
        model = Trip
        fields = ['trip_branch', 'trip_number', 'ticket_number', 'trip_zone', 'trip_sub_location', 'trip_field',
                  'trip_date',
                  'tractor_or_lorry', 'trip_driver', 'field_in', 'field_out', 'loaded_by_1', 'loading_driver_1',
                  'loaded_by_2', 'loading_driver_2', 'weight_in', 'weight_out', 'trip_type']
        widgets = {
            'trip_date': DateInput(),
            'time_in': forms.TimeInput(format="%H:%M"),
            'time_out': forms.TimeInput(format="%H:%M"),
        }


class FuelConsumptionForm(forms.ModelForm):
    branch_of_origin = forms.ModelChoiceField(label='Branch', queryset=Branch.objects.all().order_by('name'),
                                              required=True, )
    date = forms.DateField(label='Date:', widget=DateInput(), )
    vehicle_fueled = forms.ModelChoiceField(label='Vehicle', queryset=Vehicle.objects.all().order_by('registration'),
                                            required=True, )
    driver = forms.ModelChoiceField(label='Driver', queryset=Employee.objects.filter(
        Q(employee_designation__designation_code='004') | Q(employee_designation__designation_code='006') |
        Q(employee_designation__designation_code='035') | Q(employee_designation__designation_code='001') |
        Q(employee_designation__designation_code='002') | Q(employee_designation__designation_code='007') |
        Q(employee_designation__designation_code='005') | Q(employee_designation__designation_code='003')
    ).order_by('employee_first_name')
                                    )
    quantity_in_litres = forms.DecimalField(min_value=0)

    def __init__(self, *args, **kwargs):
        super(FuelConsumptionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('branch_of_origin', css_class="col-sm-3"),
                    Div('date', css_class='col-sm-2'),
                    Div('vehicle_fueled', css_class="col-sm-2"),
                    Div('driver', css_class="col-sm-3"),
                    Div('quantity_in_litres', css_class="col-sm-2"),

                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("fuel_consumption")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),
                css_class="container"
            )
        )

    class Meta:
        model = FuelConsumption
        fields = ['branch_of_origin', 'date', 'vehicle_fueled', 'driver', 'quantity_in_litres']
        widgets = {
            'date': DateInput(),
        }


class TowingForm(forms.ModelForm):
    branch_of_origin = forms.ModelChoiceField(label='Branch', queryset=Branch.objects.all().order_by('name'),
                                              required=True, )
    date = forms.DateField(label='Date:', widget=DateInput(), )
    winch = forms.ModelChoiceField(label='Winch',
                                   queryset=Vehicle.objects.filter(body_type__type='PL').order_by('registration'), )
    driver = forms.ModelChoiceField(label='Driver', queryset=Employee.objects.filter(
        employee_designation__designation_code='003').order_by('employee_first_name'))

    def __init__(self, *args, **kwargs):
        super(TowingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('branch_of_origin', css_class='col-sm-3'),
                    Div('date', css_class='col-sm-4'),
                    Div('winch', css_class='col-sm-3'),
                    css_class="row"
                ),
                Div(
                    Div('driver', css_class='col-sm-4'),
                    Div('number_of_tows', css_class='col-sm-4'),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("towing")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class="row"
                ),
                css_class="container"
            )
        )

    class Meta:
        model = Towing
        fields = ['branch_of_origin', 'date', 'winch', 'driver', 'number_of_tows']
        widgets = {
            'date': DateInput()
        }


class PackedCaneForm(forms.ModelForm):
    branch_of_origin = forms.ModelChoiceField(label='Branch', queryset=Branch.objects.all().order_by('name'),
                                              required=True, )
    date = forms.DateField(label='Date:', widget=DateInput(), )
    trip_zone = forms.ModelChoiceField(label='Zone', queryset=Zone.objects.all().order_by('name'), required=False)
    trip_sub_location = forms.ModelChoiceField(label="Sub Location",
                                               queryset=SubLocation.objects.all().order_by('sub_location'),
                                               required=False)
    trip_field = forms.ModelChoiceField(label="Field", queryset=Field.objects.all().order_by('name'), required=False)
    tractor = forms.ModelChoiceField(label='Tractor',
                                     queryset=Vehicle.objects.filter(body_type__type='TR').order_by('registration'),
                                     required=True)
    driver = forms.ModelChoiceField(label='Driver', queryset=Employee.objects.filter(
        employee_designation__designation_code='004').order_by('employee_first_name'))
    loaded_by_1 = forms.ModelChoiceField(label='Loaded by 1', queryset=Vehicle.objects.filter(
        Q(body_type__type='CM') | Q(body_type__type='BL')).order_by('registration'), required=True)
    loaded_by_2 = forms.ModelChoiceField(label='Loaded by 2', queryset=Vehicle.objects.filter(
        Q(body_type__type='CM') | Q(body_type__type='BL')).order_by('registration'), required=False)
    loading_driver_1 = forms.ModelChoiceField(label='Loading Driver 1', queryset=Employee.objects.filter(
        Q(employee_designation__designation_code='001') | Q(employee_designation__designation_code='002')).order_by(
        'employee_first_name'), required=True, )
    loading_driver_2 = forms.ModelChoiceField(label='Loading Driver 2', queryset=Employee.objects.filter(
        Q(employee_designation__designation_code='001') | Q(employee_designation__designation_code='002')).order_by(
        'employee_first_name'), required=False, )
    stacks = forms.IntegerField(
        min_value=0
    )

    def __init__(self, *args, **kwargs):
        super(PackedCaneForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('branch_of_origin', css_class="col-sm-2"),
                    Div('delivery_note', css_class="col-sm-2"),
                    Div('date', css_class="col-sm-3"),
                    Div('trip_zone', css_class="col-sm-2"),
                    Div('trip_sub_location', css_class="col-sm-2"),
                    css_class="row"
                ),
                Div(
                    Div('trip_field', css_class="col-sm-2"),
                    Div('tractor', css_class="col-sm-2"),
                    Div('driver', css_class="col-sm-3"),
                    Div('loaded_by_1', css_class="col-sm-2"),
                    Div('loading_driver_1', css_class="col-sm-2"),
                    css_class="row"
                ),
                Div(

                    Div('loaded_by_2', css_class="col-sm-4"),
                    Div('loading_driver_2', css_class="col-sm-6"),
                    Div('stacks', css_class="col-sm-2"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("packed_cane")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class="row"
                ),
                css_class="container"
            )
        )

    class Meta:
        model = PackedCane
        fields = ['branch_of_origin', 'delivery_note', 'date', 'trip_zone', 'trip_sub_location', 'trip_field',
                  'tractor',
                  'driver', 'loaded_by_1', 'loading_driver_1', 'loaded_by_2', 'loading_driver_2', 'stacks']
        widgets = {
            'date': DateInput()
        }


# LoadersDailyEntry Form
class LoadersDailyEntryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LoadersDailyEntryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div('date', css_class="col-sm-2"),
                layout.HTML(f'<br>'),
                Div('loader_name', css_class="col-sm-4"),
                layout.HTML(f'<br>'),
                Div('worked', css_class="col-sm-3"),
                bootstrap.FormActions(
                    layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                    layout.HTML(
                        f'<a href="{reverse("loaders_entry")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                ),
                css_class="row"
            )
        )

    class Meta:
        model = LoadersDailyEntry
        fields = ['date', 'loader_name', 'worked']
        widgets = {
            'date': DateInput()
        }


# PickupsAndCantersControl
class PickupsAndCantersControlForm(forms.ModelForm):
    vehicle_name = forms.ModelChoiceField(label="Vehicle", queryset=Vehicle.objects.filter(
        Q(body_type__type='CN') | Q(body_type__type='PU')).order_by('registration'), required=True)
    driver = forms.ModelChoiceField(label="Driver", queryset=Employee.objects.filter(
        Q(employee_designation__designation_code='006') | Q(employee_designation__designation_code='007')).order_by(
        'employee_first_name'))

    def __init__(self, *args, **kwargs):
        super(PickupsAndCantersControlForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div("date", css_class="col-sm-3"),
                    Div("vehicle_name", css_class="col-sm-3"),
                    Div("driver", css_class="col-sm-3"),
                    css_class="row"
                ),
                Div(
                    Div("opening_reading", css_class="col-sm-3"),
                    Div("closing_reading", css_class="col-sm-3"),
                    Div("milage", css_class="col-sm-3"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("pickup_canter_control")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class="row"
                ),
                css_class="container"
            )
        )

    class Meta:
        model = PickupsAndCantersControl
        fields = ['date', 'vehicle_name', 'driver', 'opening_reading', 'closing_reading', 'milage']
        widgets = {
            'date': DateInput()
        }


# TicketReconciliation
class TicketReconciliationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TicketReconciliationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('ticket_trip', css_class="col-sm-4"),
                    css_class="row"
                ),
                Div(
                    Div('paid', css_class="col-sm-4"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("ticket_reconciliation")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class="row"
                ),
                css_class="container"
            )
        )

    class Meta:
        model = TicketReconciliation
        fields = ['ticket_trip', 'paid']


# TrailerAttachment
class TrailerAttachmentForm(forms.ModelForm):
    tractor = forms.ModelChoiceField(label='Tractor',
                                     queryset=Vehicle.objects.filter(body_type__type='TR').order_by('registration'))
    trailer = forms.ModelChoiceField(label='Tractor',
                                     queryset=Vehicle.objects.filter(Q(body_type__type='HT') | Q(body_type__type='TD') |
                                                                     Q(body_type__type='TO') | Q(body_type__type='TS') |
                                                                     Q(body_type__type='TT')).order_by('registration'))

    def __init__(self, *args, **kwargs):
        super(TrailerAttachmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('tractor', css_class="col-sm-4"),
                    Div('trailer', css_class="col-sm-4"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("trailer_attachment")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class="row"
                ),
                css_class="container"
            )
        )

    class Meta:
        model = TrailerAttachment
        fields = ['tractor', 'trailer']
        widgets = {
            'date': DateInput()
        }


# InsuranceRisk
class InsuranceRiskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InsuranceRiskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'

    class Meta:
        model = InsuranceRisk
        fields = ['name', 'description']


# InsuranceCompany
class InsuranceCompanyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InsuranceCompanyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'

    class Meta:
        model = InsuranceCompany
        fields = ['name']


# InsuranceValidity
class InsuranceValidityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InsuranceValidityForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('certificate_number', css_class="col-sm-3"),
                    Div('vehicle_name', css_class="col-sm-3"),
                    Div('policy_no', css_class="col-sm-3"),
                    Div('policy_type', css_class="col-sm-3"),
                    css_class="row"
                ),
                Div(
                    Div('commence_date', css_class="col-sm-3"),
                    Div('expiry_date', css_class="col-sm-3"),
                    Div('delivery_note_no', css_class="col-sm-2"),
                    Div('risk_covered', css_class="col-sm-2"),
                    Div('insured_by', css_class="col-sm-2"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("insurance_validity")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class="row"
                ),
                css_class="container"
            )
        )

    class Meta:
        model = InsuranceValidity
        fields = ['certificate_number', 'vehicle_name', 'policy_no', 'policy_type', 'commence_date', 'expiry_date',
                  'delivery_note_no', 'risk_covered', 'insured_by']
        widgets = {
            'commence_date': DateInput(),
            'expiry_date': DateInput(),
        }


# DrivingLicenceValidity
class DrivingLicenceValidityForm(forms.ModelForm):
    driver = forms.ModelChoiceField(queryset=Employee.objects.filter(
        Q(employee_designation__designation_code='004') | Q(employee_designation__designation_code='006') |
        Q(employee_designation__designation_code='035') | Q(employee_designation__designation_code='001') |
        Q(employee_designation__designation_code='002') | Q(employee_designation__designation_code='007') |
        Q(employee_designation__designation_code='005') | Q(employee_designation__designation_code='003')
    ).order_by('employee_first_name'))

    def __init__(self, *args, **kwargs):
        super(DrivingLicenceValidityForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('driver', css_class="col-sm-4"),
                    Div('active_date', css_class='col-sm-4'),
                    Div('expiry_date', css_class='col-sm-4'),
                    css_class="row"
                ),
                Div(
                    Div('licence_no', css_class="col-sm-3"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("driving_licence_validity")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class="row"
                ),
                css_class="container"
            )
        )

    class Meta:
        model = DrivingLicenceValidity
        fields = ['driver', 'active_date', 'expiry_date', 'licence_no']
        widgets = {
            'active_date': DateInput(),
            'expiry_date': DateInput(),
        }
