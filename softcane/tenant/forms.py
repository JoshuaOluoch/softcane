from .models import Tenant, VehicleType, Vehicle
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
#from bootstrap_datepicker_plus import DatePickerInput

class DateInput(forms.DateInput):
	input_type = 'date'
	format = "%Y/%m/%d"

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['name','subdomain','postal_code','telephone','email','pin_number','vat_number','payroll_date','is_active']
        widgets = {
            'payroll_date':DateInput()
        }


class VehicleTypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VehicleTypeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'
    class Meta:
        model = VehicleType
        fields = ['type','description']

class VehicleTypeEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VehicleTypeEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'
    class Meta:
        model = VehicleType
        fields = ['type','description']
        widgets = {'description':forms.Textarea()}


class VehicleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'
    class Meta:
        model = Vehicle
        fields = ['code','registration','make','vehicle_model','body_type','body_color']
