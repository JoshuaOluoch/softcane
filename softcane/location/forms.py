from .models import Zone, SubLocation, Field
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from location.models import Branch, Zone, SubLocation, Field
from tenant.models import TenantAwareModel
from users.models import User
from django import forms
from django.db.models import Q
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import Div
from crispy_forms import bootstrap, layout
from django.urls import reverse
from crispy_forms.layout import Layout, Submit


class BranchForm(forms.ModelForm):
    name = forms.CharField(label='Name',required=True)
    description = forms.CharField(label='Description',required=False)
    address = forms.DecimalField(label='Address', required=False)

    def __init__(self, *args, **kwargs):
        super(BranchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('name', css_class="col-sm-3"),
                    Div('description', css_class='col-sm-4'),
                    Div('address', css_class="col-sm-5"),

                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("branch")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),
                css_class="container"
            )
        )

    class Meta:
        model = Branch
        fields = ['name', 'description', 'address']


class ZoneForm(forms.ModelForm):
    name = forms.CharField(label='Name',required=True)
    lower_range = forms.DecimalField(label='Lower Range',required=True,min_value=0)
    upper_range = forms.DecimalField(label='Upper Range',required=True,min_value=0)
    amount = forms.DecimalField(label='Amount',required=True,min_value=0)

    def __init__(self, *args, **kwargs):
        super(ZoneForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('name', css_class="col-sm-3"),
                    Div('lower_range', css_class='col-sm-3'),
                    Div('upper_range', css_class="col-sm-3"),
                    Div('amount', css_class="col-sm-3"),

                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("zones")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),
                css_class="container"
            )
        )

    class Meta:
        model = Zone
        fields = ['name', 'lower_range', 'upper_range', 'amount']


class SubLocationForm(forms.ModelForm):
    code = forms.CharField(label='Code',required=True)
    sub_location = forms.CharField(label='Sub Location',required=True)

    def __init__(self, *args, **kwargs):
        super(SubLocationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            Div(
                Div(
                    Div('code', css_class="col-sm-6"),
                    Div('sub_location', css_class='col-sm-6'),

                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("sublocation")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),
                css_class="container"
            )
        )

    class Meta:
        model = SubLocation
        fields = ['code', 'sub_location']


class FieldForm(forms.ModelForm):
    field_code = forms.CharField(label='Field Code',required=True)
    name = forms.CharField(label='Field Name',required=True)
    sub_location = forms.ModelChoiceField(label='Sub Location', queryset=SubLocation.objects.all().order_by('sub_location'), required=True)
    distance = forms.DecimalField(label='Distance',required=True, min_value=0)

    def __init__(self, *args, **kwargs):
        super(FieldForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('field_code', css_class="col-sm-3"),
                    Div('name', css_class="col-sm-3"),
                    Div('sub_location', css_class="col-sm-3"),
                    Div('distance', css_class="col-sm-3"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("field")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),

                css_class='container'
            )

        )

    class Meta:
        model = Field
        fields = ['field_code', 'name', 'sub_location', 'distance']
