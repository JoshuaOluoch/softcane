from django.contrib import admin
from .models import (AccountsGroupingListing, AccountsHeadingsListing, AssetsGroupingListing,
                     AssetsRegisterListing, TenantCustomer, TenantSupplier, VatCodesListing,
                     GeneralLedgerListing, JournalEntry, ReceivePayment, MakePayment, CustomerTransaction,
                     SupplierTransaction)

admin.site.register(AccountsGroupingListing)
admin.site.register(AccountsHeadingsListing)
admin.site.register(AssetsGroupingListing)
admin.site.register(AssetsRegisterListing)
admin.site.register(TenantCustomer)
admin.site.register(TenantSupplier)
admin.site.register(VatCodesListing)
admin.site.register(GeneralLedgerListing)
admin.site.register(JournalEntry)
admin.site.register(ReceivePayment)
admin.site.register(MakePayment)
admin.site.register(CustomerTransaction)
admin.site.register(SupplierTransaction)



