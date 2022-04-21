from django.urls import path, include
from .views import (account_headings_view, account_headings_create_view,AccountHeadingsUpdateView, AccountsHeadingsDeleteView,
                    account_groupings_view, account_groupings_create_view, AccountGroupingsUpdateView, AccountGroupingsDeleteView,
                    general_ledger_view, general_ledger_create_view, GeneralLedgerUpdateView, GeneralLedgerDeleteView,
                    asset_groupings_view, asset_groupings_create_view,AssetGroupingsUpdateView, AssetGroupingsDeleteView,
                    asset_register_view, asset_register_create_view, AssetRegisterUpdateView, AssetRegisterDeleteView,
                    vat_codes_view, vat_codes_create_view, VatCodesUpdateView, VatCodesDeleteView,
                    customer_view, customer_create_view, CustomerUpdateView, CustomerDeleteView,
                    supplier_view, supplier_create_view, SupplierUpdateView, SupplierDeleteView,
                    journal_entry_view, journal_entry_create_view, JournalEntryUpdateView, JournalEntryDeleteView,
                    payment_receipt_view, payment_receipt_create_view,ReceivePaymentUpdateView, ReceivePaymentDeleteView,
                    payment_made_view, payment_made_create_view, MakePaymentUpdateView, MakePaymentDeleteView,
                    customer_transaction_view, customer_transaction_create_view, CustomerTransactionUpdateView, CustomerTransactionDeleteView,
                    supplier_transaction_view, supplier_transaction_create_view, SupplierTransactionUpdateView, SupplierTransactionDeleteView)


urlpatterns = [
    #Account headings url
    path('', account_headings_view, name="account_headings"),
    path('account_headings_create/',account_headings_create_view, name = 'account_headings_create'),
    path('<pk>/account_headings_update/', AccountHeadingsUpdateView.as_view(), name = 'account_headings_update'),
    path('<pk>/account_headings_delete/',AccountsHeadingsDeleteView.as_view(), name = 'account_headings_delete'),
    #Account Groupings urls
    path('account_groupings/', account_groupings_view, name="account_groupings"),
    path('account_groupings_create/', account_groupings_create_view, name='account_groupings_create'),
    path('account_groupings/<pk>/account_groupings_update/', AccountGroupingsUpdateView.as_view(), name='account_groupings_update'),
    path('account_groupings/<pk>/account_groupings_delete/', AccountGroupingsDeleteView.as_view(), name='account_groupings_delete'),
    #General Ledger urls
    path('general_ledger/', general_ledger_view, name="general_ledger"),
    path('general_ledger_create/',general_ledger_create_view, name = 'general_ledger_create'),
    path('general_ledger/<pk>/general_ledger_update/', GeneralLedgerUpdateView.as_view(), name = 'general_ledger_update'),
    path('general_ledger/<pk>/general_ledger_delete/',GeneralLedgerDeleteView.as_view(), name = 'general_ledger_delete'),
    #Asset Groupings url
    path('asset_groupings/', asset_groupings_view, name="asset_groupings"),
    path('asset_groupings_create/',asset_groupings_create_view, name = 'asset_groupings_create'),
    path('asset_groupings/<pk>/asset_groupings_update/', AssetGroupingsUpdateView.as_view(), name = 'asset_groupings_update'),
    path('asset_groupings/<pk>/asset_groupings_delete/',AssetGroupingsDeleteView.as_view(), name = 'asset_groupings_delete'),
    #Asset Register urls
    path('asset_register/', asset_register_view, name="asset_register"),
    path('asset_register_create/', asset_register_create_view, name='asset_register_create'),
    path('asset_register/<pk>/asset_register_update/', AssetRegisterUpdateView.as_view(), name='asset_register_update'),
    path('asset_register/<pk>/asset_register_delete/', AssetRegisterDeleteView.as_view(), name='asset_register_delete'),
    #VAT codes urls
    path('vat_codes/', vat_codes_view, name="vat_codes"),
    path('vat_code_create/',vat_codes_create_view, name = 'vat_code_create'),
    path('vat_codes/<pk>/vat_code_update/', VatCodesUpdateView.as_view(), name = 'vat_code_update'),
    path('vat_codes/<pk>/vat_code_delete/',VatCodesDeleteView.as_view(), name = 'vat_code_delete'),
    #Customer urls
    path('customers/', customer_view, name="customers"),
    path('customer_create/', customer_create_view, name='customer_create'),
    path('customers/<pk>/customer_update/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/<pk>/customer_delete/', CustomerDeleteView.as_view(), name='customer_delete'),
    #Supplier urls
    path('suppliers/', supplier_view, name="suppliers"),
    path('supplier_create/',supplier_create_view, name = 'supplier_create'),
    path('suppliers/<pk>/supplier_update/', SupplierUpdateView.as_view(), name = 'supplier_update'),
    path('suppliers/<pk>/supplier_delete/',SupplierDeleteView.as_view(), name = 'supplier_delete'),
    #Journal Entry urls
    path('journal_entry/', journal_entry_view, name="journal_entry"),
    path('journal_entry_create/',journal_entry_create_view, name = 'journal_entry_create'),
    path('journal_entry/<pk>/journal_entry_update/', JournalEntryUpdateView.as_view(), name = 'journal_entry_update'),
    path('journal_entry/<pk>/journal_entry_delete/',JournalEntryDeleteView.as_view(), name = 'journal_entry_delete'),
    #Payment Receipt urls
    path('payment_receipt/', payment_receipt_view, name="payment_receipt"),
    path('payment_receipt_create/',payment_receipt_create_view, name = 'payment_receipt_create'),
    path('payment_receipt/<pk>/payment_receipt_update/', ReceivePaymentUpdateView.as_view(), name = 'payment_receipt_update'),
    path('payment_receipt/<pk>/payment_receipt_delete/',ReceivePaymentDeleteView.as_view(), name = 'payment_receipt_delete'),
    #Payment Made urls
    path('payment_made/', payment_made_view, name="payment_made"),
    path('payment_made_create/',payment_made_create_view, name = 'payment_made_create'),
    path('payment_made/<pk>/payment_made_update/', MakePaymentUpdateView.as_view(), name = 'payment_made_update'),
    path('payment_made/<pk>/payment_made_delete/',MakePaymentDeleteView.as_view(), name = 'payment_made_delete'),
    #Customer Transactions urls
    path('customer_transaction/', customer_transaction_view, name="customer_transaction"),
    path('customer_transaction_create/',customer_transaction_create_view, name = 'customer_transaction_create'),
    path('customer_transaction/<pk>/customer_transaction_update/', CustomerTransactionUpdateView.as_view(), name = 'customer_transaction_update'),
    path('customer_transaction/<pk>/customer_transaction_delete/',CustomerTransactionDeleteView.as_view(), name = 'customer_transaction_delete'),
    #Supplier Transactions urls
    path('supplier_transaction/', supplier_transaction_view, name="supplier_transaction"),
    path('supplier_transaction_create/',supplier_transaction_create_view, name = 'supplier_transaction_create'),
    path('supplier_transaction/<pk>/supplier_transaction_update/', SupplierTransactionUpdateView.as_view(), name = 'supplier_transaction_update'),
    path('supplier_transaction/<pk>/supplier_transaction_delete/',SupplierTransactionDeleteView.as_view(), name = 'supplier_transaction_delete'),
]
