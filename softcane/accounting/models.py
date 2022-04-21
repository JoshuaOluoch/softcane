from django.db import models
from tenant.models import TenantAwareModel
from .bank_list import BANKCHOICES
from django.utils.timezone import now

from users.models import User


class AccountsHeadingsListing(TenantAwareModel):
    accounts_heading_listing_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description


DEFAULT_ACCOUNT_HEADING_ID = 1


class AccountsGroupingListing(TenantAwareModel):
    accounts_grouping_listing_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255, blank=True)
    classification = models.ForeignKey(AccountsHeadingsListing, on_delete=models.CASCADE,
                                       default=DEFAULT_ACCOUNT_HEADING_ID)

    def __str__(self):
        return self.description


class GeneralLedgerListing(TenantAwareModel):
    general_ledger_listing_id = models.AutoField(primary_key=True)
    acc_no = models.CharField(max_length=10)
    description = models.CharField(max_length=255, blank=True)
    sub_group = models.ForeignKey(AccountsGroupingListing, on_delete=models.CASCADE, default=DEFAULT_ACCOUNT_HEADING_ID)
    debit = models.DecimalField(max_digits=200, decimal_places=2)
    credit = models.DecimalField(max_digits=200, decimal_places=2)
    balance = models.DecimalField(max_digits=200, decimal_places=2)

    def __str__(self):
        return self.description


class AssetsGroupingListing(TenantAwareModel):
    assets_grouping_listing_id = models.AutoField(primary_key=True)
    group_id = models.CharField(max_length=10)
    description = models.CharField(max_length=255, blank=True)
    depreciation = models.DecimalField(max_digits=20, decimal_places=5)

    def __str__(self):
        return self.description


class AssetsRegisterListing(TenantAwareModel):
    assets_register_listing_id = models.AutoField(primary_key=True)
    acc_no = models.CharField(max_length=10)
    description = models.CharField(max_length=255, blank=True)
    group = models.ForeignKey(AssetsGroupingListing, on_delete=models.CASCADE, default=DEFAULT_ACCOUNT_HEADING_ID)
    value = models.DecimalField(max_digits=20, decimal_places=5)

    def __str__(self):
        return self.description


class VatCodesListing(TenantAwareModel):
    vat_codes_listing_id = models.AutoField(primary_key=True)
    vat_code = models.CharField(max_length=10, blank=True)
    rate = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.CharField(max_length=255, blank=True)

    def __str_(self):
        return self.description


class TenantCustomer(TenantAwareModel):
    tenant_customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255, blank=True)
    customer_postal_code = models.CharField(max_length=255, blank=True, default=" ")
    customer_telephone = models.CharField(max_length=255, blank=True, default=" ")
    customer_email = models.EmailField(max_length=255, blank=True, default="example@email.com")
    customer_pin_number = models.CharField(max_length=255, blank=True, default=" ")
    customer_vat_number = models.CharField(max_length=255, blank=True, default=" ")

    def __str__(self):
        return self.customer_name


class TenantSupplier(TenantAwareModel):
    supplier_customer_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=255, blank=True)
    supplier_postal_code = models.CharField(max_length=255, blank=True, default="")
    supplier_telephone = models.CharField(max_length=255, blank=True, default="")
    supplier_email = models.EmailField(max_length=255, blank=True, default="")
    supplier_pin_number = models.CharField(max_length=255, blank=True, default="")
    supplier_vat_number = models.CharField(max_length=255, blank=True, default="")

    def __str__(self):
        return self.supplier_name


class BankAccounts(TenantAwareModel):
    bank_account_id = models.AutoField(primary_key=True)
    bank_account = models.CharField(max_length=255, unique=True)
    bank_account_description = models.CharField(max_length=255, unique=True)
    bank_name = models.CharField(max_length=255, choices=BANKCHOICES, default='Bank of Baroda')


"""
Here we will define the models involved in the transactions. The models are as follows
1. Journal Entry (Transaction No, Date, Debit, Reference, Amount, Narration, Credit)
2. Receive Payments : Transaction No, Date, Received From,Amount, Narration, Paid to 
3. Customer Transactions : Transaction No, Transaction Type, Date, Reference,Customer,Amount, VAT, Narration, Account No
4. Supplier Transactions: Transaction No, Transaction Type, Date, Reference,Supplier,Amount, VAT, Narration, Account No
5. Make Payments: Transaction No, Date, Account paid, Reference, Amount, Narration, Paid From
"""


class JournalEntry(TenantCustomer):
    journal_entry_id = models.AutoField(primary_key=True)
    transaction_no = models.CharField(max_length=128, unique=True)
    date = models.DateField(default=now)
    debit_account = models.ForeignKey(TenantCustomer, on_delete=models.CASCADE, related_name='+')
    reference = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    narration = models.CharField(max_length=255)
    credit_account = models.ForeignKey(TenantCustomer, on_delete=models.CASCADE, related_name='+')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    posted_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.transaction_no


class ReceivePayment(TenantAwareModel):
    received_payment_id = models.AutoField(primary_key=True)
    transaction_no = models.CharField(max_length=128, unique=True)
    date = models.DateField(default=now)
    received_from = models.ForeignKey(TenantCustomer, on_delete=models.CASCADE)
    reference = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    narration = models.CharField(max_length=255)
    paid_to = models.ForeignKey(BankAccounts, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    posted_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.transaction_no


class CustomerTransaction(TenantAwareModel):
    customer_transaction_id = models.AutoField(primary_key=True)
    transaction_no = models.CharField(max_length=128, unique=True)
    transaction_type = models.CharField(max_length=128, choices=[('INVOICE', 'INVOICE'), ('CR/TR', 'CR/TR'), ],
                                        default='INVOICE')
    date = models.DateField(default=now)
    customer = models.ForeignKey(TenantCustomer, on_delete=models.CASCADE)
    reference = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    vat = models.ForeignKey(VatCodesListing, on_delete=models.CASCADE)
    narration = models.CharField(max_length=255)
    gl_account = models.ForeignKey(BankAccounts, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    posted_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.transaction_no


class SupplierTransaction(TenantAwareModel):
    customer_transaction_id = models.AutoField(primary_key=True)
    transaction_no = models.CharField(max_length=128, unique=True)
    transaction_type = models.CharField(max_length=128, choices=[('INVOICE', 'INVOICE'), ('CR/TR', 'CR/TR'), ],
                                        default='INVOICE')
    date = models.DateField(default=now)
    supplier = models.ForeignKey(TenantSupplier, on_delete=models.CASCADE)
    reference = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    vat = models.ForeignKey(VatCodesListing, on_delete=models.CASCADE)
    narration = models.CharField(max_length=255)
    gl_account = models.ForeignKey(BankAccounts, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    posted_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.transaction_no


class MakePayment(TenantAwareModel):
    make_payment_id = models.AutoField(primary_key=True)
    transaction_no = models.CharField(max_length=128, unique=True)
    date = models.DateField(default=now)
    supplier_account = models.ForeignKey(TenantSupplier, on_delete=models.CASCADE)
    reference = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    narration = models.CharField(max_length=255)
    paid_to = models.ForeignKey(BankAccounts, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    posted_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.transaction_no
