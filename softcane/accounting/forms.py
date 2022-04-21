from .models import (AccountsGroupingListing, AccountsHeadingsListing, AssetsGroupingListing,
                     AssetsRegisterListing, TenantCustomer, TenantSupplier, VatCodesListing,
                     GeneralLedgerListing, JournalEntry, ReceivePayment, MakePayment, CustomerTransaction,
                     SupplierTransaction)

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from accounting.models import *
from tenant.models import TenantAwareModel
from users.models import User
from django import forms
from django.db.models import Q
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import Div
from crispy_forms import bootstrap, layout
from django.urls import reverse
from crispy_forms.layout import Layout, Submit


class AccountsHeadingsForm(forms.ModelForm):
    code = forms.CharField(label='Code', required=True)
    description = forms.CharField(label='Description', required=True)

    def __init__(self, *args, **kwargs):
        super(AccountsHeadingsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('code', css_class="col-sm-3"),
                    Div('description', css_class="col-sm-9"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("account_headings")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),

                css_class='container'
            )

        )

    class Meta:
        model = AccountsHeadingsListing
        fields = ['code', 'description']


class AccountsGroupingForm(forms.ModelForm):
    code = forms.CharField(label='Code', required=True)
    description = forms.CharField(label='Description', required=True)
    classification = forms.ModelChoiceField(label='Classification',
                                            queryset=AccountsHeadingsListing.objects.all().order_by('description'),
                                            required=True)

    def __init__(self, *args, **kwargs):
        super(AccountsGroupingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            Div(
                Div(
                    Div('code', css_class="col-sm-2"),
                    Div('description', css_class="col-sm-6"),
                    Div('classification', css_class="col-sm-4"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("account_groupings")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),

                css_class='container'
            )

        )

    class Meta:
        model = AccountsGroupingListing
        fields = ['code', 'description', 'classification']


class GeneralLedgerForm(forms.ModelForm):
    acc_no = forms.CharField(label='Account No.', required=True)
    description = forms.CharField(label='Description', required=True)
    sub_group = forms.ModelChoiceField(label='Sub Group',
                                       queryset=AccountsGroupingListing.objects.all().order_by('description'),
                                       required=True)
    debit = forms.DecimalField(label='Debit', min_value=0, required=True)
    credit = forms.DecimalField(label='Credit', min_value=0, required=True)
    balance = forms.DecimalField(label='Balance', min_value=0, required=True)

    def __init__(self, *args, **kwargs):
        super(GeneralLedgerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            Div(
                Div(
                    Div('acc_no', css_class="col-sm-4"),
                    Div('description', css_class="col-sm-4"),
                    Div('sub_group', css_class="col-sm-4"),
                    css_class='row'
                ),
                Div(
                    Div('debit', css_class="col-sm-4"),
                    Div('credit', css_class="col-sm-4"),
                    Div('balance', css_class="col-sm-4"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("general_ledger")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),
                css_class='container'
            )
        )

    class Meta:
        model = GeneralLedgerListing
        fields = ['acc_no', 'description', 'sub_group', 'debit', 'credit', 'balance']


class AssetsGroupingForm(forms.ModelForm):
    group_id = forms.CharField(label='Group ID', required=True)
    description = forms.CharField(label='Description', required=True)
    depreciation = forms.DecimalField(label='Depreciation', min_value=0, required=True)

    def __init__(self, *args, **kwargs):
        super(AssetsGroupingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            Div(
                Div(
                    Div('group_id', css_class="col-sm-4"),
                    Div('description', css_class="col-sm-4"),
                    Div('depreciation', css_class="col-sm-4"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("asset_groupings")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),

                css_class='container'
            )
        )

    class Meta:
        model = AssetsGroupingListing
        fields = ['group_id', 'description', 'depreciation']


class AssetsRegisterForm(forms.ModelForm):
    acc_no = forms.CharField(label='Account No', required=True)
    description = forms.CharField(label='Description', required=True)
    group = forms.ModelChoiceField(label='Group ID',
                                   queryset=AssetsGroupingListing.objects.all().order_by('description'), required=True)
    value = forms.DecimalField(label='Value', min_value=0, required=True)

    def __init__(self, *args, **kwargs):
        super(AssetsRegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            Div(
                Div(
                    Div('acc_no', css_class="col-sm-3"),
                    Div('description', css_class="col-sm-3"),
                    Div('group', css_class="col-sm-3"),
                    Div('value', css_class="col-sm-3"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("asset_register")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),
                css_class='container'
            )
        )

    class Meta:
        model = AssetsRegisterListing
        fields = ['acc_no', 'description', 'group', 'value']


class VatCodesForm(forms.ModelForm):
    vat_code = forms.CharField(label='V.A.T Code', required=True)
    rate = forms.DecimalField(label='Rate', min_value=0, required=True)
    description = forms.CharField(label='Description', required=True)

    def __init__(self, *args, **kwargs):
        super(VatCodesForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            Div(
                Div(
                    Div('vat_code', css_class="col-sm-3"),
                    Div('rate', css_class="col-sm-3"),
                    Div('description', css_class="col-sm-3"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("vat_codes")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),

                css_class='container'
            )
        )

    class Meta:
        model = VatCodesListing
        fields = ['vat_code', 'rate', 'description']


class TenantCustomerForm(forms.ModelForm):
    customer_name = forms.CharField(label='Customer Name', required=True)
    customer_postal_code = forms.CharField(label="Customer Postal Code", required=True)
    customer_telephone = forms.CharField(label='Customer Telephone No', required=True)
    customer_email = forms.EmailField(label='Customer Email', required=True)
    customer_pin_number = forms.CharField(label='Customer K.R.A Number', required=True)
    customer_vat_number = forms.CharField(label='Customer V.A.T Number', required=True)

    def __init__(self, *args, **kwargs):
        super(TenantCustomerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            Div(
                Div(
                    Div('customer_name', css_class="col-sm-4"),
                    Div('customer_postal_code', css_class="col-sm-4"),
                    Div('customer_telephone', css_class="col-sm-4"),
                    css_class='row'
                ),
                Div(
                    Div('customer_email', css_class="col-sm-4"),
                    Div('customer_pin_number', css_class="col-sm-4"),
                    Div('customer_vat_number', css_class="col-sm-4"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("customers")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),

                css_class='container'
            )
        )

    class Meta:
        model = TenantCustomer
        fields = ['customer_name', 'customer_postal_code', 'customer_telephone', 'customer_email',
                  'customer_pin_number', 'customer_vat_number']


class TenantSupplierForm(forms.ModelForm):
    supplier_name = forms.CharField(label='Supplier Name', required=True)
    supplier_postal_code = forms.CharField(label="Supplier Postal Code", required=True)
    supplier_telephone = forms.CharField(label='Supplier Telephone No', required=True)
    supplier_email = forms.EmailField(label='Supplier Email', required=True)
    supplier_pin_number = forms.CharField(label='Supplier K.R.A Number', required=True)
    supplier_vat_number = forms.CharField(label='Supplier V.A.T Number', required=True)

    def __init__(self, *args, **kwargs):
        super(TenantSupplierForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            Div(
                Div(
                    Div('supplier_name', css_class="col-sm-4"),
                    Div('supplier_postal_code', css_class="col-sm-4"),
                    Div('supplier_telephone', css_class="col-sm-4"),
                    css_class='row'
                ),
                Div(
                    Div('supplier_email', css_class="col-sm-4"),
                    Div('supplier_pin_number', css_class="col-sm-4"),
                    Div('supplier_vat_number', css_class="col-sm-4"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("suppliers")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class='row'
                ),

                css_class='container'
            )
        )

    class Meta:
        model = TenantSupplier
        fields = ['supplier_name', 'supplier_postal_code', 'supplier_telephone', 'supplier_email',
                  'supplier_pin_number', 'supplier_vat_number']


# Transactions Forms
# 1.JournalEntry
class JournalEntryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JournalEntryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('transaction_no', css_class="col-sm-3"),
                    Div('date', css_class="col-sm-3"),
                    Div('debit_account', css_class="col-sm-3"),
                    Div('reference', css_class="col-sm-3"),
                    css_class="row"
                ),
                Div(
                    Div('amount', css_class="col-sm-3"),
                    Div('narration', css_class="col-sm-5"),
                    Div('credit_account', css_class="col-sm-3"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("journal_entry")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class="row"
                ),
                css_class="container"
            )
        )

    class Meta:
        model = JournalEntry
        fields = ['transaction_no', 'date', 'debit_account', 'reference', 'amount', 'narration', 'credit_account']


# 2.ReceivePayment
class ReceivePaymentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReceivePaymentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('transaction_no', css_class="col-sm-3"),
                    Div('date', css_class="col-sm-3"),
                    Div('received_from', css_class="col-sm-3"),
                    Div('reference', css_class="col-sm-3"),
                    css_class="row"
                ),
                Div(
                    Div('amount', css_class="col-sm-3"),
                    Div('narration', css_class="col-sm-5"),
                    Div('paid_to', css_class="col-sm-3"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("payment_receipt")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class="row"
                ),
                css_class="container"
            )
        )

    class Meta:
        model = ReceivePayment
        fields = ['transaction_no', 'date', 'received_from', 'reference', 'amount', 'narration', 'paid_to']


# 3.CustomerTransactionForm
class CustomerTransactionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomerTransactionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('transaction_no', css_class="col-sm-3"),
                    Div('transaction_type', css_class="col-sm-3"),
                    Div('date', css_class="col-sm-3"),
                    Div('customer', css_class="col-sm-3"),

                    css_class="row"
                ),
                Div(
                    Div('reference', css_class="col-sm-3"),
                    Div('amount', css_class="col-sm-3"),
                    Div('vat', css_class="col-sm-3"),
                    Div('narration', css_class="col-sm-3"),
                    css_class="row"
                ),

                Div(
                    Div('gl_account', css_class="col-sm-3"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("customer_transaction")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class="row"
                ),
                css_class="container"
            )
        )

    class Meta:
        model = CustomerTransaction
        fields = ['transaction_no', 'transaction_type', 'date', 'customer', 'reference', 'amount', 'vat', 'narration',
                  'gl_account']


# 4.SupplierTransactionForm
class SupplierTransactionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SupplierTransactionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('transaction_no', css_class="col-sm-3"),
                    Div('transaction_type', css_class="col-sm-3"),
                    Div('date', css_class="col-sm-3"),
                    Div('supplier', css_class="col-sm-3"),

                    css_class="row"
                ),
                Div(
                    Div('reference', css_class="col-sm-3"),
                    Div('amount', css_class="col-sm-3"),
                    Div('vat', css_class="col-sm-3"),
                    Div('narration', css_class="col-sm-3"),
                    css_class="row"
                ),

                Div(
                    Div('gl_account', css_class="col-sm-3"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("supplier_transaction")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class="row"
                ),
                css_class="container"
            )
        )

    class Meta:
        model = SupplierTransaction
        fields = ['transaction_no', 'transaction_type', 'date', 'supplier', 'reference', 'amount', 'vat', 'narration',
                  'gl_account']


# 5.MakePayment
class MakePaymentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MakePaymentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('transaction_no', css_class="col-sm-3"),
                    Div('date', css_class="col-sm-3"),
                    Div('supplier_account', css_class="col-sm-3"),
                    Div('reference', css_class="col-sm-3"),
                    css_class="row"
                ),
                Div(
                    Div('amount', css_class="col-sm-3"),
                    Div('narration', css_class="col-sm-5"),
                    Div('paid_to', css_class="col-sm-3"),
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Submit', css_class='btn btn-primary'),
                        layout.HTML(
                            f'<a href="{reverse("make_payment")}" class="btn btn-outline-secondary">{("Cancel")}</a>')
                    ),
                    css_class="row"
                ),
                css_class="container"
            )
        )

    class Meta:
        model = MakePayment
        fields = ['transaction_no', 'date', 'supplier_account', 'reference', 'amount', 'narration', 'paid_to']
