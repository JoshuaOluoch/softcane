from django.shortcuts import render
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
import django_tables2 as tables
from django_tables2.export.views import ExportMixin

from .table import *
from transport.models import *
from stock.models import *
from .filters import *
from .forms import *


class FilteredSingleTableView(SingleTableMixin, FilterView):
    formhelper_class = None

    def get_filterset(self, filterset_class):
        kwargs = self.get_filterset_kwargs(filterset_class)
        filterset = filterset_class(**kwargs)
        filterset.form.helper = self.formhelper_class()
        return filterset


class TripListView(ExportMixin, FilteredSingleTableView):
    model = Trip
    table_class = TripTable
    paginate_by = 25
    template_name = "report/trip_report.html"
    filterset_class = TripFilter
    formhelper_class = TripFilterFormHelper


class ParkedCaneListView(ExportMixin, FilteredSingleTableView):
    model = PackedCane
    table_class = ParkedCaneTable
    paginate_by = 25
    template_name = "report/parked_cane_report.html"
    filterset_class = ParkedCaneFilter
    formhelper_class = ParkedCaneFilterFormHelper


class LoadersListView(ExportMixin, FilteredSingleTableView):
    model = LoadersDailyEntry
    table_class = LoadersTable
    paginate_by = 25
    template_name = "report/loaders_report.html"
    filterset_class = LoadersFilter
    formhelper_class = LoadersFilterFormHelper


class TowingListView(ExportMixin, FilteredSingleTableView):
    model = Towing
    table_class = TowingTable
    paginate_by = 25
    template_name = "report/towing_report.html"
    filterset_class = TowingFilter
    formhelper_class = TowingFilterFormHelper


class PickupsAndCanterControlListView(ExportMixin, FilteredSingleTableView):
    model = PickupsAndCantersControl
    table_class = PickupsAndCanterControlTable
    paginate_by = 25
    template_name = "report/PickupsAndCanterControl_report.html"
    filterset_class = PickupsAndCantersControlFilter
    formhelper_class = PickupsAndCanterControlFilterFormHelper


class TicketReconciliationListView(ExportMixin, FilteredSingleTableView):
    model = TicketReconciliation
    table_class = TicketReconciliationTable
    paginate_by = 25
    template_name = "report/ticket_reconciliation_report.html"
    filterset_class = TicketReconciliationFilter
    formhelper_class = TicketReconciliationFilterFormHelper


class TrailerAttachmentListView(ExportMixin, FilteredSingleTableView):
    model = TrailerAttachment
    table_class = TrailerAttachmentTable
    paginate_by = 25
    template_name = "report/trailer_attachment_report.html"
    filterset_class = TrailerAttachmentFilter
    formhelper_class = TrailerAttachmentFilterFormHelper


class DrivingLicenceValidityListView(ExportMixin, FilteredSingleTableView):
    model = DrivingLicenceValidity
    table_class = DrivingLicenceValidityTable
    paginate_by = 25
    template_name = "report/driving_licence_report.html"
    filterset_class = DrivingLicenceValidityFilter
    formhelper_class = DrivingLicenceValidityFilterFormHelper


class JournalEntryListView(ExportMixin, FilteredSingleTableView):
    model = JournalEntry
    table_class = JournalEntryTable
    paginate_by = 25
    template_name = "report/journal_entry_report.html"
    filterset_class = JournalEntryFilter
    formhelper_class = JournalEntryFilterFormHelper


class CustomerTransactionListView(ExportMixin, FilteredSingleTableView):
    model = CustomerTransaction
    table_class = CustomerTransactionTable
    paginate_by = 25
    template_name = "report/customer_transaction_report.html"
    filterset_class = CustomerTransactionFilter
    formhelper_class = CustomerTransactionFilterFormHelper


class SupplierTransactionListView(ExportMixin, FilteredSingleTableView):
    model = SupplierTransaction
    table_class = SupplierTransactionTable
    paginate_by = 25
    template_name = "report/supplier_transaction_report.html"
    filterset_class = SupplierTransactionFilter
    formhelper_class = SupplierTransactionFilterFormHelper


class ReceivePaymentListView(ExportMixin, FilteredSingleTableView):
    model = ReceivePayment
    table_class = ReceivePaymentTable
    paginate_by = 25
    template_name = "report/receive_payment_report.html"
    filterset_class = ReceivePaymentFilter
    formhelper_class = ReceivePaymentFilterFormHelper


class MakePaymentListView(ExportMixin, FilteredSingleTableView):
    model = MakePayment
    table_class = MakePaymentTable
    paginate_by = 25
    template_name = "report/make_payment_report.html"
    filterset_class = MakePaymentFilter
    formhelper_class = MakePaymentFilterFormHelper


class AttendanceListView(ExportMixin, FilteredSingleTableView):
    model = Attendance
    table_class = AttendanceTable
    paginate_by = 25
    template_name = "report/attendance_report.html"
    filterset_class = AttendanceFilter
    formhelper_class = AttendanceFilterFormHelper


class AllowancesDeductionsListView(ExportMixin, FilteredSingleTableView):
    model = AllowanceAndDeductions
    table_class = AllowancesDeductionsTable
    paginate_by = 25
    template_name = "report/allowances_deductions_report.html"
    filterset_class = AllowancesDeductionsFilter
    formhelper_class = AllowancesDeductionsFilterFormHelper


class HolidayPayListView(ExportMixin, FilteredSingleTableView):
    model = HolidayPay
    table_class = HolidayPayTable
    paginate_by = 25
    template_name = "report/holidaypay_report.html"
    filterset_class = HolidayPayFilter
    formhelper_class = HolidayPayFilterFormHelper


class FuelReadingsListView(ExportMixin, FilteredSingleTableView):
    model = FuelReadings
    table_class = FuelReadingsTable
    paginate_by = 25
    template_name = "report/fuel_readings_report.html"
    filterset_class = FuelReadingsFilter
    formhelper_class = FuelReadingsFilterFormHelper


class StockArticleReceiptListView(ExportMixin, FilteredSingleTableView):
    model = StockArticleReceipt
    table_class = StockArticleReceiptTable
    paginate_by = 25
    template_name = "report/stock_article_receipt.html"
    filterset_class = StockArticleReceiptFilter
    formhelper_class = StockArticleReceiptFilterFormHelper


class StockArticleIssueListView(ExportMixin, FilteredSingleTableView):
    model = StockArticleIssue
    table_class = StockArticleIssueTable
    paginate_by = 25
    template_name = "report/stock_article_issue.html"
    filterset_class = StockArticleIssueFilter
    formhelper_class = StockArticleIssueFilterFormHelper


class StockArticleAdjustmentListView(ExportMixin, FilteredSingleTableView):
    model = StockArticleAdjustment
    table_class = StockArticleAdjustmentTable
    paginate_by = 25
    template_name = "report/stock_adjustment_report.html"
    filterset_class = StockArticleAdjustmentFilter
    formhelper_class = StockArticleAdjustmentFilterFormHelper


class FuelConsumptionListView(ExportMixin, FilteredSingleTableView):
    model = FuelConsumption
    table_class = FuelConsumptionTable
    paginate_by = 25
    template_name = "report/fuel_consumption_report.html"
    filterset_class = FuelConsumptionFilter
    formhelper_class = FuelConsumptionFilterFormHelper


class InsuranceValidityListView(ExportMixin, FilteredSingleTableView):
    model = InsuranceValidity
    table_class = InsuranceValidityTable
    paginate_by = 25
    template_name = "report/insurance_validity_report.html"
    filterset_class = InsuranceValidityFilter
    formhelper_class = InsuranceValidityFilterFormHelper
