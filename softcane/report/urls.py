from django.urls import path, include
from .views import *

urlpatterns =[
    path('trip_report/', TripListView.as_view(), name="trip_report"),
    path('parked_cane_report/', ParkedCaneListView.as_view(), name="parked_cane_report"),
    path('loaders_report/', LoadersListView.as_view(), name="loaders_report"),
    path('towing_report/', TowingListView.as_view(), name="towing_report"),
    path('pickups_canter_control_report/', PickupsAndCanterControlListView.as_view(), name="pickups_canter_control_report"),
    path('trailer_attachment_report/', TrailerAttachmentListView.as_view(), name="trailer_attachment_report"),
    path('ticket_reconciliation_report/', TicketReconciliationListView.as_view(), name="ticket_reconciliation_report"),
    path('driving_licence_report/', DrivingLicenceValidityListView.as_view(), name="driving_licence_report"),
    #accounting report
    path('journal_entries_report/', JournalEntryListView.as_view(), name="journal_entries_report"),
    path('customer_transaction_report/', CustomerTransactionListView.as_view(), name="customer_transaction_report"),
    path('supplier_transaction_report/', SupplierTransactionListView.as_view(), name="supplier_transaction_report"),
    path('receive_payment_report/', ReceivePaymentListView.as_view(), name="receive_payment_report"),
    path('make_payment_report/', MakePaymentListView.as_view(), name="make_payment_report"),
    #attendance report
    path('attendance_report/', AttendanceListView.as_view(), name="attendance_report"),
    #allowances & Deduction report
    path('allowances_deductions_report/', AllowancesDeductionsListView.as_view(), name="allowances_deductions_report"),
    #holiday pay
    path('holidaypay_report/', HolidayPayListView.as_view(), name="holidaypay_report"),
    #Fuel readings
    path('fuel_readings_report/', FuelReadingsListView.as_view(), name="fuel_readings_report"),
    #stock article report
    path('stock_article_report/', StockArticleReceiptListView.as_view(), name="stock_article_report"),
    #stock report issue
    path('stock_issue_report/', StockArticleIssueListView.as_view(), name="stock_issue_report"),
    #stock report issue
    path('stock_adjustment_report/', StockArticleAdjustmentListView.as_view(), name="stock_adjustment_report"),
    #stock report issue
    path('fuel_consumption_report/', FuelConsumptionListView.as_view(), name="fuel_consumption_report"),
    #insurance validity report
    path('insurance_validity_report/', InsuranceValidityListView.as_view(), name="insurance_validity_report"),

]