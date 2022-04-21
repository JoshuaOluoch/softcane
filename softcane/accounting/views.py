from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.urls import reverse_lazy
from .models import (AccountsHeadingsListing, AccountsGroupingListing, GeneralLedgerListing,
                     AssetsGroupingListing, AssetsRegisterListing, VatCodesListing,
                     TenantSupplier, TenantCustomer, JournalEntry, ReceivePayment, MakePayment, CustomerTransaction,
                     SupplierTransaction)
from tenant.utilities import get_tenant
from .forms import (AccountsHeadingsForm, AccountsGroupingForm, GeneralLedgerForm, AssetsGroupingForm,
                    AssetsRegisterForm,
                    VatCodesForm, TenantCustomerForm, TenantSupplierForm, JournalEntryForm, ReceivePaymentForm,
                    MakePaymentForm,
                    CustomerTransactionForm, SupplierTransactionForm)
from django.views.generic.detail import DetailView
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    ListView,
    DeleteView,
    TemplateView
)


# Account Headings Views
@login_required()
def account_headings_view(request):
    tenant = get_tenant(request)
    account_headings = AccountsHeadingsListing.objects.filter(tenant=tenant)

    return render(request, 'accounting/account_headings.html', {'account_headings': account_headings, 'tenant': tenant})


@login_required()
def account_headings_create_view(request):
    form = AccountsHeadingsForm()
    if request.method == 'POST':
        form = AccountsHeadingsForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/accounting/')
        else:
            form = AccountsHeadingsForm()
    return render(request, 'accounting/account_headings_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class AccountHeadingsUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/account_headings_update.html'
    form_class = AccountsHeadingsForm
    success_url = reverse_lazy('account_headings')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(AccountsHeadingsListing, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class AccountsHeadingsDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/account_headings_delete.html'
    success_url = reverse_lazy('account_headings')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(AccountsHeadingsListing, pk=pk_)


# Account Groupings Views
@login_required()
def account_groupings_view(request):
    tenant = get_tenant(request)
    account_groupings = AccountsGroupingListing.objects.filter(tenant=tenant)

    return render(request, 'accounting/account_groupings.html',
                  {'account_groupings': account_groupings, 'tenant': tenant})


@login_required()
def account_groupings_create_view(request):
    form = AccountsGroupingForm()
    if request.method == 'POST':
        form = AccountsGroupingForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/accounting/account_groupings/')
        else:
            form = AccountsGroupingForm()
    return render(request, 'accounting/account_groupings_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class AccountGroupingsUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/account_groupings_update.html'
    form_class = AccountsGroupingForm
    success_url = reverse_lazy('account_groupings')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(AccountsGroupingListing, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class AccountGroupingsDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/account_groupings_delete.html'
    success_url = reverse_lazy('account_groupings')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(AccountsGroupingListing, pk=pk_)


# General Ledger Views
@login_required()
def general_ledger_view(request):
    tenant = get_tenant(request)
    general_ledgers = GeneralLedgerListing.objects.filter(tenant=tenant)

    return render(request, 'accounting/general_ledger.html', {'general_ledgers': general_ledgers, 'tenant': tenant})


@login_required()
def general_ledger_create_view(request):
    form = GeneralLedgerForm()
    if request.method == 'POST':
        form = GeneralLedgerForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/accounting/general_ledger/')
        else:
            form = GeneralLedgerForm()
    return render(request, 'accounting/general_ledger_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class GeneralLedgerUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/general_ledger_update.html'
    form_class = GeneralLedgerForm
    success_url = reverse_lazy('general_ledger')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(GeneralLedgerListing, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class GeneralLedgerDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/general_ledger_delete.html'
    success_url = reverse_lazy('general_ledger')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(GeneralLedgerListing, pk=pk_)


# Asset Groupings Views
@login_required()
def asset_groupings_view(request):
    tenant = get_tenant(request)
    asset_groupings = AssetsGroupingListing.objects.filter(tenant=tenant)

    return render(request, 'accounting/asset_groupings.html', {'asset_groupings': asset_groupings, 'tenant': tenant})


@login_required()
def asset_groupings_create_view(request):
    form = AssetsGroupingForm()
    if request.method == 'POST':
        form = AssetsGroupingForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/accounting/asset_groupings/')
        else:
            form = AssetsGroupingForm()
    return render(request, 'accounting/asset_groupings_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class AssetGroupingsUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/asset_groupings_update.html'
    form_class = AssetsGroupingForm
    success_url = reverse_lazy('asset_groupings')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(AssetsGroupingListing, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class AssetGroupingsDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/asset_groupings_delete.html'
    success_url = reverse_lazy('asset_groupings')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(AssetsGroupingListing, pk=pk_)


# Asset Register Views
@login_required()
def asset_register_view(request):
    tenant = get_tenant(request)
    asset_register = AssetsRegisterListing.objects.filter(tenant=tenant)

    return render(request, 'accounting/asset_register.html', {'asset_register': asset_register, 'tenant': tenant})


@login_required()
def asset_register_create_view(request):
    form = AssetsRegisterForm()
    if request.method == 'POST':
        form = AssetsRegisterForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/accounting/asset_register/')
        else:
            form = AssetsRegisterForm()
    return render(request, 'accounting/asset_register_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class AssetRegisterUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/asset_register_update.html'
    form_class = AssetsRegisterForm
    success_url = reverse_lazy('asset_register')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(AssetsRegisterListing, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class AssetRegisterDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/asset_register_delete.html'
    success_url = reverse_lazy('asset_register')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(AssetsRegisterListing, pk=pk_)


# VAT Codes Views
@login_required()
def vat_codes_view(request):
    tenant = get_tenant(request)
    vat_codes = VatCodesListing.objects.filter(tenant=tenant)

    return render(request, 'accounting/vat_codes.html', {'vat_codes': vat_codes, 'tenant': tenant})


@login_required()
def vat_codes_create_view(request):
    form = VatCodesForm()
    if request.method == 'POST':
        form = VatCodesForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/accounting/vat_codes/')
        else:
            form = VatCodesForm()
    return render(request, 'accounting/vat_codes_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class VatCodesUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/vat_codes_update.html'
    form_class = VatCodesForm
    success_url = reverse_lazy('vat_codes')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(VatCodesListing, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class VatCodesDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/vat_codes_delete.html'
    success_url = reverse_lazy('vat_codes')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(VatCodesListing, pk=pk_)


# Tenant Supplier Views
@login_required()
def supplier_view(request):
    tenant = get_tenant(request)
    suppliers = TenantSupplier.objects.filter(tenant=tenant)

    return render(request, 'accounting/suppliers.html', {'suppliers': suppliers, 'tenant': tenant})


@login_required()
def supplier_create_view(request):
    form = TenantSupplierForm()
    if request.method == 'POST':
        form = TenantSupplierForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/accounting/suppliers/')
        else:
            form = TenantSupplierForm()
    return render(request, 'accounting/supplier_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/supplier_update.html'
    form_class = TenantSupplierForm
    success_url = reverse_lazy('suppliers')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(TenantSupplier, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/supplier_delete.html'
    success_url = reverse_lazy('suppliers')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(TenantSupplier, pk=pk_)


# Tenant Customer Views
@login_required()
def customer_view(request):
    tenant = get_tenant(request)
    customers = TenantCustomer.objects.filter(tenant=tenant)

    return render(request, 'accounting/customers.html', {'customers': customers, 'tenant': tenant})


@login_required()
def customer_create_view(request):
    form = TenantCustomerForm()
    if request.method == 'POST':
        form = TenantCustomerForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/accounting/customers/')
        else:
            form = TenantCustomerForm()
    return render(request, 'accounting/customer_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/customer_update.html'
    form_class = TenantCustomerForm
    success_url = reverse_lazy('customers')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(TenantCustomer, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/customer_delete.html'
    success_url = reverse_lazy('customers')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(TenantCustomer, pk=pk_)


######################################################################################################################
#################################Accounting Transactions Views ########################################################
# Journal Entry Views
@login_required()
def journal_entry_view(request):
    tenant = get_tenant(request)
    journal_entry = JournalEntry.objects.filter(tenant=tenant)

    return render(request, 'accounting/journal_entry.html', {'journal_entry': journal_entry, 'tenant': tenant})


@login_required()
def journal_entry_create_view(request):
    form = JournalEntryForm()
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/accounting/journal_entry/')
        else:
            form = JournalEntryForm()
    return render(request, 'accounting/journal_entry_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class JournalEntryUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/journal_entry_update.html'
    form_class = JournalEntryForm
    success_url = reverse_lazy('journal_entry')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(JournalEntry, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class JournalEntryDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/journal_entry_delete.html'
    success_url = reverse_lazy('journal_entry')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(JournalEntry, pk=pk_)


# Receive Payments Views
@login_required()
def payment_receipt_view(request):
    tenant = get_tenant(request)
    payment_receipt = ReceivePayment.objects.filter(tenant=tenant)

    return render(request, 'accounting/payment_receipt.html', {'payment_receipt': payment_receipt, 'tenant': tenant})


@login_required()
def payment_receipt_create_view(request):
    form = ReceivePaymentForm()
    if request.method == 'POST':
        form = ReceivePaymentForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/accounting/payment_receipt/')
        else:
            form = ReceivePaymentForm()
    return render(request, 'accounting/payment_receipt_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class ReceivePaymentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/payment_receipt_update.html'
    form_class = ReceivePaymentForm
    success_url = reverse_lazy('payment_receipt')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(ReceivePayment, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class ReceivePaymentDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/payment_receipt_delete.html'
    success_url = reverse_lazy('payment_receipt')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(ReceivePayment, pk=pk_)


# Payment Made Views
@login_required()
def payment_made_view(request):
    tenant = get_tenant(request)
    payment_made = MakePayment.objects.filter(tenant=tenant)

    return render(request, 'accounting/payment_made.html', {'payment_made': payment_made, 'tenant': tenant})


@login_required()
def payment_made_create_view(request):
    form = MakePaymentForm()
    if request.method == 'POST':
        form = MakePaymentForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/accounting/payment_made/')
        else:
            form = MakePaymentForm()
    return render(request, 'accounting/payment_made_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class MakePaymentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/payment_made_update.html'
    form_class = MakePaymentForm
    success_url = reverse_lazy('payment_made')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(MakePayment, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class MakePaymentDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/payment_made_delete.html'
    success_url = reverse_lazy('payment_made')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(MakePayment, pk=pk_)


# Customer Transaction Views
@login_required()
def customer_transaction_view(request):
    tenant = get_tenant(request)
    customer_transactions = CustomerTransaction.objects.filter(tenant=tenant)

    return render(request, 'accounting/customer_transaction.html',
                  {'customer_transactions': customer_transactions, 'tenant': tenant})


@login_required()
def customer_transaction_create_view(request):
    form = CustomerTransactionForm()
    if request.method == 'POST':
        form = CustomerTransactionForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/accounting/customer_transaction/')
        else:
            form = CustomerTransactionForm()
    return render(request, 'accounting/customer_transaction_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class CustomerTransactionUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/customer_transaction_update.html'
    form_class = CustomerTransactionForm
    success_url = reverse_lazy('customer_transaction')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(CustomerTransaction, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class CustomerTransactionDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/customer_transaction_delete.html'
    success_url = reverse_lazy('customer_transaction')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(CustomerTransaction, pk=pk_)


# Supplier Transaction Views
@login_required()
def supplier_transaction_view(request):
    tenant = get_tenant(request)
    supplier_transactions = SupplierTransaction.objects.filter(tenant=tenant)

    return render(request, 'accounting/supplier_transaction.html',
                  {'supplier_transactions': supplier_transactions, 'tenant': tenant})


@login_required()
def supplier_transaction_create_view(request):
    form = SupplierTransactionForm()
    if request.method == 'POST':
        form = SupplierTransactionForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/accounting/supplier_transaction/')
        else:
            form = SupplierTransactionForm()
    return render(request, 'accounting/supplier_transaction_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class SupplierTransactionUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/supplier_transaction_update.html'
    form_class = SupplierTransactionForm
    success_url = reverse_lazy('supplier_transaction')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(SupplierTransaction, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class SupplierTransactionDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounting/supplier_transaction_delete.html'
    success_url = reverse_lazy('supplier_transaction')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(SupplierTransaction, pk=pk_)
