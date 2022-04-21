import django_filters
from transport.models import *
from accounting.models import *
from hr.models import *
from stock.models import *
from django import forms


class TripFilter(django_filters.FilterSet):
    trip_date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Trip
        fields = ['trip_branch', 'trip_date']


class ParkedCaneFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PackedCane
        fields = ['branch_of_origin', 'date']


class LoadersFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = LoadersDailyEntry
        fields = ['loader_name', 'date']


class TowingFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Towing
        fields = ['branch_of_origin', 'date']


class PickupsAndCantersControlFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PickupsAndCantersControl
        fields = ['driver', 'date']


class TicketReconciliationFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = TicketReconciliation
        fields = ['ticket_trip', 'date']


class TrailerAttachmentFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = TrailerAttachment
        fields = ['trailer', 'date']


class DrivingLicenceValidityFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = DrivingLicenceValidity
        fields = ['driver']


class JournalEntryFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = JournalEntry
        fields = ['reference']


class CustomerTransactionFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = CustomerTransaction
        fields = ['reference']


class SupplierTransactionFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = SupplierTransaction
        fields = ['reference']


class ReceivePaymentFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = ReceivePayment
        fields = ['reference']


class MakePaymentFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = MakePayment
        fields = ['reference']


class AttendanceFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Attendance
        fields = ['name']


class AllowancesDeductionsFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = AllowanceAndDeductions
        fields = ['name']


class HolidayPayFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = HolidayPay
        fields = ['name']


class FuelReadingsFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = FuelReadings
        fields = ['fuel_pump']


class StockArticleReceiptFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = StockArticleReceipt
        fields = ['reference_no']


class StockArticleIssueFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = StockArticleIssue
        fields = ['reference_no']


class StockArticleAdjustmentFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = StockArticleAdjustment
        fields = ['reference_no']


class FuelConsumptionFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = FuelConsumption
        fields = ['driver']


class InsuranceValidityFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = InsuranceValidity
        fields = ['insured_by']
