from .models import (Designation, Department, Employee, TransportPayrollRate,
                     PayrollCode, PayeBand, NhifBand, Loader, Attendance, AllowanceAndDeductions, HolidayPay)

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from hr.models import Designation
from tenant.models import TenantAwareModel
from users.models import User
from django import forms
from django.db.models import Q
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django.forms.models import formset_factory
from crispy_forms import layout, bootstrap
from crispy_forms.bootstrap import InlineField, FormActions, StrictButton, Div
from crispy_forms.layout import Layout
from crispy_forms import bootstrap, layout
from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form
from django.urls import reverse
from django.core.exceptions import ValidationError
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Fieldset, HTML, Layout, Submit


class DateInput(forms.DateInput):
    input_type = 'date'
    format = "%Y-%m-%d"


class DesignationForm(forms.ModelForm):
    designation_code = forms.CharField(
        label='Designation Code',
        required=True)
    description = forms.CharField(
        label='Descriptions',

        required=True)

    def __init__(self, *args, **kwargs):
        super(DesignationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(Div(
                Div('designation_code', css_class="col-sm-3"),
                Div('description', css_class='col-sm-9'),
                bootstrap.FormActions(
                    layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                    layout.HTML(
                        f'<a href="{reverse("designation")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                ),
                css_class='row'
            ),
                css_class="container"
            )
        )

    class Meta:
        model = Designation
        fields = ['designation_code', 'description']


class DepartmentForm(forms.ModelForm):
    department_category = forms.CharField(
        label='Department Category',
        required=True)
    department_description = forms.CharField(
        label='Department Description',
        required=True)
    department_narration = forms.CharField(
        label='Department Narration',
        required=True)

    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(Div(
                Div('department_category', css_class="col-sm-3"),
                Div('department_description', css_class='col-sm-3'),
                Div('department_narration', css_class='col-sm-6'),
                bootstrap.FormActions(
                    layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                    layout.HTML(
                        f'<a href="{reverse("department")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                ),
                css_class='row'
            ),
                css_class="container"

            )
        )

    class Meta:
        model = Department
        fields = ['department_category', 'department_description', 'department_narration']


class EmployeeForm(forms.ModelForm):
    employee_code = forms.CharField(
        label='Employee Code',
        required=True)
    employee_first_name = forms.CharField(
        label='First Name',
        required=True)
    employee_last_name = forms.CharField(
        label='Last Name',
        required=True)
    employee_designation = forms.ModelChoiceField(
        label='Designation',
        queryset=Designation.objects.all().order_by('designation_code'),
        required=True)
    employee_department = forms.ModelChoiceField(
        label='Department',
        queryset=Department.objects.all().order_by('department_category'),
        required=True)
    employee_id_number = forms.CharField(
        label='ID Number',
        required=True)
    employee_kra_pin = forms.CharField(
        label='KRA PIN',
        required=True)
    employee_address = forms.CharField(
        label='Employee Address',
        required=True)
    employee_account_number = forms.CharField(
        label='Account Number',
        required=True)
    employee_nhif_no = forms.CharField(
        label='NHIF No.',
        required=False)
    employee_nssf_no = forms.CharField(
        label='NSSF No.',
        required=False)
    employee_union = forms.CharField(
        label='Union',
        required=False)
    employee_contact = forms.CharField(
        label='Contact',
        required=False)
    employee_next_of_kin = forms.CharField(
        label='Next of kin',
        required=False)
    employee_next_of_kin_contact = forms.CharField(
        label='Next of kin contact',
        required=False)

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('employee_code', css_class="col-sm-4"),
                    Div('employee_first_name', css_class='col-sm-4'),
                    Div('employee_last_name', css_class='col-sm-4'),
                    css_class='row'
                ),
                Div(
                    Div('employee_designation', css_class="col-sm-4"),
                    Div('employee_department', css_class='col-sm-4'),
                    Div('employee_id_number', css_class='col-sm-4'),
                    css_class='row'
                ),
                Div(
                    Div('employee_kra_pin', css_class="col-sm-3"),
                    Div('employee_account_number', css_class='col-sm-4'),
                    Div('employee_sex', css_class='col-sm-2'),
                    Div('employee_nhif_no', css_class="col-sm-3"),
                    css_class='row'
                ),
                Div(
                    Div('employee_nssf_no', css_class="col-sm-2"),
                    Div('employee_union', css_class='col-sm-2'),
                    Div('employee_contact', css_class='col-sm-2'),
                    Div('employee_next_of_kin', css_class="col-sm-3"),
                    Div('employee_next_of_kin_contact', css_class="col-sm-3"),
                    css_class='row'
                ),
                Div(
                    Div('active', css_class='col-sm-2'),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("employee")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),

                css_class='container'
            )
        )

    class Meta:
        model = Employee
        fields = ['employee_code', 'employee_first_name', 'employee_last_name', 'employee_designation',
                  'employee_department', 'employee_id_number', 'employee_kra_pin', 'employee_sex', 'employee_nhif_no',
                  'employee_nssf_no', 'employee_union', 'employee_contact', 'employee_next_of_kin',
                  'employee_next_of_kin_contact',
                  'employee_address', 'employee_account_number', 'active']


class TransportPayrollRateForm(forms.ModelForm):
    single_bundle = forms.DecimalField(label='Single Bundle', required=True, min_value=0)
    double_bundle = forms.DecimalField(label='Double Bundle', required=True, min_value=0)
    weighing_clerk_bundle = forms.DecimalField(label='Weighing Clerk Bundle', required=True, min_value=0)
    field_clerk_bundle = forms.DecimalField(label='Field Clerk Bundle', required=True, min_value=0)
    cameco_operator = forms.DecimalField(label='Cameco Operator', required=True, min_value=0)
    bell_operator = forms.DecimalField(label='Bell Operator', required=True, min_value=0)
    winch_operator = forms.DecimalField(label='Winch Operator', required=True, min_value=0)
    loader_rate = forms.DecimalField(label='Loader Rate', required=True, min_value=0)

    def __init__(self, *args, **kwargs):
        super(TransportPayrollRateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('single_bundle', css_class="col-sm-2"),
                    Div('double_bundle', css_class='col-sm-2'),
                    Div('weighing_clerk_bundle', css_class='col-sm-4'),
                    Div('field_clerk_bundle', css_class="col-sm-4"),
                    css_class='row'
                ),
                Div(
                    Div('cameco_operator', css_class='col-sm-4'),
                    Div('bell_operator', css_class='col-sm-4'),
                    Div('winch_operator', css_class="col-sm-2"),
                    Div('loader_rate', css_class='col-sm-2'),

                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("transport_payroll")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),

                css_class='container'

            )
        )

    class Meta:
        model = TransportPayrollRate
        fields = ['single_bundle', 'double_bundle', 'weighing_clerk_bundle', 'field_clerk_bundle', 'cameco_operator',
                  'bell_operator', 'winch_operator', 'loader_rate']


class PayrollCodeForm(forms.ModelForm):
    payroll_code = forms.CharField(label='Payroll Code', required=True)
    payroll_description = forms.CharField(label='Payroll Description', required=True)
    payroll_usage = forms.CharField(label='Payroll Usage', required=True)

    def __init__(self, *args, **kwargs):
        super(PayrollCodeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            Div(
                Div(
                    Div('payroll_code', css_class='col-sm-4'),
                    Div('payroll_description', css_class='col-sm-4'),
                    Div('payroll_usage', css_class="col-sm-4"),

                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("payroll_code")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),

                css_class='container'

            )
        )

    class Meta:
        model = PayrollCode
        fields = ['payroll_code', 'payroll_description', 'payroll_usage']


class PayeBandForm(forms.ModelForm):
    paye_band_tax = forms.DecimalField(label='Paye Band Tax', required=True, min_value=0)
    paye_band_description = forms.CharField(label='Paye Band Description', required=True)
    paye_band_lower_range = forms.DecimalField(label='Lower Range', required=True, min_value=0)
    paye_band_upper_range = forms.DecimalField(label='Upper Range', required=True, min_value=0)
    paye_band_amount = forms.DecimalField(label='Paye Band Amount', required=True, min_value=0)

    def __init__(self, *args, **kwargs):
        super(PayeBandForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('paye_band_tax', css_class='col-sm-2'),
                    Div('paye_band_description', css_class='col-sm-3'),
                    Div('paye_band_lower_range', css_class="col-sm-2"),
                    Div('paye_band_upper_range', css_class="col-sm-2"),
                    Div('paye_band_amount', css_class="col-sm-3"),

                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("paye_band")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),

                css_class='container'

            )
        )

    class Meta:
        model = PayeBand
        fields = ['paye_band_tax', 'paye_band_description', 'paye_band_lower_range', 'paye_band_upper_range',
                  'paye_band_amount']


class NhifBandForm(forms.ModelForm):
    nhif_band_description = forms.CharField(label='NHIF Band Description', required=True)
    nhif_band_lower_range = forms.DecimalField(label='NHIF lower Range', required=True, min_value=0)
    nhif_band_upper_range = forms.DecimalField(label='NHIF upper Range', required=True, min_value=0)
    nhif_band_amount = forms.DecimalField(label='NHIF band Range', required=True, min_value=0)
    effective_date = forms.DateField(label='Effective Date', widget=DateInput(), )

    def __init__(self, *args, **kwargs):
        super(NhifBandForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('nhif_band_description', css_class='col-sm-3'),
                    Div('nhif_band_lower_range', css_class='col-sm-2'),
                    Div('nhif_band_upper_range', css_class="col-sm-2"),
                    Div('nhif_band_amount', css_class="col-sm-2"),
                    Div('effective_date', css_class="col-sm-3"),

                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("nhif_band")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),

                css_class='container'

            )
        )

    class Meta:
        model = NhifBand
        fields = ['nhif_band_description', 'nhif_band_lower_range', 'nhif_band_upper_range', 'nhif_band_amount',
                  'effective_date']

        widgets = {
            'effective_date': DateInput(),
        }


class LoaderForm(forms.ModelForm):
    name = forms.ModelChoiceField(
        label='Loader',
        queryset=Employee.objects.filter(employee_designation__designation_code='005').order_by('employee_first_name'),
        required=True)
    date_registered = forms.DateField(label='Date Registered', widget=DateInput(), )

    def __init__(self, *args, **kwargs):
        super(LoaderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('name', css_class='col-sm-4'),
                    Div('date_registered', css_class='col-sm-4'),
                    Div('active', css_class="col-sm-4"),

                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("loader")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),

                css_class='container'

            )
        )

    class Meta:
        model = Loader
        fields = ['name', 'date_registered', 'active']

        widgets = {
            'date_registered': DateInput(),
        }


class AttendanceForm(forms.ModelForm):
    """
    employee_code = forms.ModelChoiceField(
        label='Employee Code',
        queryset=Employee.objects.all(),
        required=True
    )

    name = forms.ModelChoiceField(
        label='Employee Name',
        queryset=Employee.objects.all().order_by('employee_first_name').filter('employee_code'),
        required=True
    )
    department_category = forms.ModelChoiceField(
        label='Department Category',
        queryset=Department.objects.all().filter('name'),
        required=True
    )
    """

    date = forms.DateField(
        label='Date',
        widget=DateInput(),
    )

    def __init__(self, *args, **kwargs):
        super(AttendanceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(

                    Div('name', css_class='col-sm-6'),
                    Div('department_category', css_class="col-sm-6"),
                    css_class="row"
                ),
                Div(
                    Div('attend', css_class='col-sm-6'),
                    Div('date', css_class='col-sm-6'),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("attendance")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),

                css_class='container'

            )
        )

    class Meta:
        model = Attendance
        fields = ['name', 'department_category', 'attend', 'date']

        widgets = {
            'date': DateInput(),
        }


class AllowanceAndDeductionsForm(forms.ModelForm):
    """
    name = forms.ModelChoiceField(label='Loader', queryset=Employee.objects.all().order_by('employee_first_name'),
                                  required=True)
    """
    amount = forms.DecimalField(
        label='Amount',
        required=True,
        min_value=0
    )
    desc = forms.CharField(
        label='Description',
        required=True,
    )
    date = forms.DateField(label='Date', widget=DateInput(), )

    def __init__(self, *args, **kwargs):
        super(AllowanceAndDeductionsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('name', css_class='col-sm-8'),
                    Div('trans_code', css_class='col-sm-4'),
                    css_class="row"
                ),
                Div(
                    Div('desc', css_class="col-sm-6"),
                    Div('date', css_class='col-sm-4'),
                    Div('amount', css_class="col-sm-2"),

                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("allowancesDeductions")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),

                css_class='container'

            )
        )

    class Meta:
        model = AllowanceAndDeductions
        fields = ['name', 'trans_code', 'desc', 'date', 'amount']

        widgets = {
            'date': DateInput(),
        }


class HolidayPayForm(forms.ModelForm):
    """
    name = forms.ModelChoiceField(label='Loader', queryset=Employee.objects.all().order_by('employee_first_name'),
                                  required=True)
    """
    amount = forms.DecimalField(
        label='Amount',
        required=True,
        min_value=0
    )

    date = forms.DateField(label='Date', widget=DateInput(), )

    def __init__(self, *args, **kwargs):
        super(HolidayPayForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('name', css_class='col-sm-8'),
                    Div('trans_code', css_class='col-sm-4'),
                    css_class="row"
                ),
                Div(
                    Div('date', css_class='col-sm-4'),
                    Div('amount', css_class="col-sm-2"),

                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("holidayPay")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),

                css_class='container'

            )
        )

    class Meta:
        model = HolidayPay
        fields = ['name', 'trans_code', 'date', 'amount']

        widgets = {
            'date': DateInput(),
        }
