from .models import (StockCategory, StockItem, FuelType, Tank, FuelPump, \
                     FuelReadings, StockArticleReceipt, StockArticleIssue, StockArticleAdjustment)
from accounting.models import TenantSupplier, TenantCustomer
from users.models import User
from django.utils.timezone import now
from location.models import Branch

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


class StockCategoryForm(forms.ModelForm):
    category = forms.CharField()
    description = forms.CharField()
    examples = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(StockCategoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('category', css_class="col-md-3"),
                    Div('description', css_class="col-md-4"),
                    Div('examples', css_class="col-md-5"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("stock_categories")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class="row"
                ),
                css_class="container"
            )
        )

    class Meta:
        model = StockCategory
        fields = ['category', 'description', 'examples']


class StockItemForm(forms.ModelForm):
    item_code = forms.CharField(label='Code')
    item_description = forms.CharField(label='Description', required=False)
    item_part_number = forms.CharField(label='Part No.', required=False)
    item_category = forms.ModelChoiceField(label='Category', queryset=StockCategory.objects.all(), required=True)

    item_price = forms.DecimalField(label='Price', decimal_places=2)

    def __init__(self, *args, **kwargs):
        super(StockItemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('item_code', css_class="col-sm-3"),
                    Div('item_description', css_class="col-sm-4"),
                    Div('item_part_number', css_class="col-sm-3"),
                    css_class="row"
                ),
                Div(
                    Div('item_category', css_class="col-sm-4"),
                    Div('item_price', css_class="col-sm-3"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("stock_items")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class="row"
                ),
                css_class="container"
            )
        )

    class Meta:
        model = StockItem
        fields = ['item_code', 'item_description', 'item_part_number', 'item_category', 'item_price']


class FuelTypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FuelTypeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div('fuel_type', css_class="col-sm-5"),
                bootstrap.FormActions(
                    layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                    layout.HTML(
                        f'<a href="{reverse("fuel_type")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                ),
                css_class="row"
            )
        )

    class Meta:
        model = FuelType
        fields = ['fuel_type']


class TankForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TankForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div('tank_code', css_class="col-sm-3"),
                Div(css_class="col-sm-1"),
                Div('fuel_type', css_class="col-sm-3"),
                Div(css_class="col-sm-1"),
                Div('tank_capacity', css_class="col-sm-3"),
                bootstrap.FormActions(
                    layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                    layout.HTML(
                        f'<a href="{reverse("tank")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                ),
                css_class="row"
            )
        )

    class Meta:
        model = Tank
        fields = ['tank_code', 'fuel_type', 'tank_capacity']


class FuelPumpForm(forms.ModelForm):
    fuel_branch = forms.ModelChoiceField(label='Branch',
                                         queryset=Branch.objects.all().order_by('name'), required=True)

    def __init__(self, *args, **kwargs):
        super(FuelPumpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div('fuel_pump_code', css_class="col-sm-4"),
                Div('fuel_pump_tank', css_class="col-sm-4"),
                Div('fuel_branch', css_class="col-sm-4"),
                bootstrap.FormActions(
                    layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                    layout.HTML(
                        f'<a href="{reverse("fuel_pump")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                ),
                css_class="row"
            )
        )

    class Meta:
        model = FuelPump
        fields = ['fuel_pump_code', 'fuel_pump_tank', 'fuel_branch']


class FuelReadingsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FuelReadingsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div('date', css_class="col-sm-4"),
                Div('fuel_pump', css_class="col-sm-4"),
                Div('morning_tank_dipping', css_class="col-sm-4"),
                Div('morning_pump_reading', css_class="col-sm-4"),
                Div('evening_tank_dipping', css_class="col-sm-4"),
                Div('evening_pump_reading', css_class="col-sm-4"),
                bootstrap.FormActions(
                    layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                    layout.HTML(
                        f'<a href="{reverse("fuel_readings")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                ),
                css_class="row"
            )
        )

    class Meta:
        model = FuelReadings
        fields = ['date', 'fuel_pump', 'morning_tank_dipping', 'morning_pump_reading', 'evening_tank_dipping',
                  'evening_pump_reading']
        widgets = {
            'date': DateInput(),
        }


# Stock Article Receipt Form
class StockArticleReceiptForm(forms.ModelForm):
    supplier_account = forms.ModelChoiceField(label='Account No', queryset=TenantSupplier.objects.all())
    supplier_name = forms.ModelChoiceField(label='Supplier Name', queryset=TenantSupplier.objects.all())

    def __init__(self, *args, **kwargs):
        super(StockArticleReceiptForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('transaction_no', css_class="col-sm-3"),
                    Div('type', css_class="col-sm-3"),
                    Div('date', css_class="col-sm-3"),
                    Div('reference_no', css_class="col-sm-3"),
                    css_class='row'
                ),
                Div(
                    Div('supplier_account', css_class="col-sm-3"),
                    Div('supplier_name', css_class="col-sm-3"),
                    Div('item', css_class="col-sm-3"),
                    Div('item_category', css_class="col-sm-3"),
                    css_class='row'
                ),
                Div(
                    Div('part_number', css_class="col-sm-3"),
                    Div('quantity_received', css_class="col-sm-2"),
                    Div('unit_cost', css_class="col-sm-3"),
                    Div('remark', css_class="col-sm-4"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("stock_article_receipt")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),
                css_class="container"
            )
        )

    class Meta:
        model = StockArticleReceipt
        fields = ['date', 'internal_no', 'reference_no', 'supplier',  'remark']
        widgets = {
            'date': DateInput(),
        }


# Stock Article Issue
class StockArticleIssueForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StockArticleIssueForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('transaction_no', css_class="col-sm-3"),
                    Div('type', css_class="col-sm-3"),
                    Div('date', css_class="col-sm-3"),
                    Div('reference_no', css_class="col-sm-3"),
                    css_class='row'
                ),
                Div(
                    Div('customer', css_class="col-sm-3"),
                    Div('item', css_class="col-sm-3"),
                    Div('item_category', css_class="col-sm-3"),
                    Div('part_number', css_class="col-sm-3"),
                    css_class='row'
                ),
                Div(
                    Div('quantity_received', css_class="col-sm-3"),
                    Div('unit_cost', css_class="col-sm-3"),
                    Div('remark', css_class="col-sm-5"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("stock_article_issue")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),
                css_class="container"
            )
        )

    class Meta:
        model = StockArticleIssue
        fields = ['transaction_no', 'type', 'date', 'reference_no', 'customer', 'item', 'item_category', 'part_number',
                  'quantity_received', 'unit_cost', 'remark']
        widgets = {
            'date': DateInput(),
        }


# Stock Articles Adjustments
class StockArticleAdjustmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StockArticleAdjustmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('transaction_no', css_class="col-sm-3"),
                    Div('type', css_class="col-sm-3"),
                    Div('date', css_class="col-sm-3"),
                    Div('reference_no', css_class="col-sm-3"),
                    css_class='row'
                ),
                Div(
                    Div('item', css_class="col-sm-3"),
                    Div('item_category', css_class="col-sm-3"),
                    Div('part_number', css_class="col-sm-3"),
                    css_class='row'
                ),
                Div(
                    Div('required_quantity', css_class="col-sm-3"),
                    Div('current_quantity', css_class="col-sm-3"),
                    Div('remark', css_class="col-sm-5"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("stock_article_adjustment")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),
                css_class="container"
            )
        )

    class Meta:
        model = StockArticleAdjustment
        fields = ['transaction_no', 'type', 'date', 'reference_no', 'item', 'item_category', 'part_number',
                  'required_quantity', 'current_quantity', 'remark']
        widgets = {
            'date': DateInput(),
        }
