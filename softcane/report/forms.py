from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button
from crispy_forms.bootstrap import Div
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'
    format = "%Y-%m-%d"


class TripFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        Div(
            Div(
                Div('trip_branch', css_class="col-sm-3"),
                Div('trip_date', css_class="col-sm-3"),
                css_class="row"
            ),
            Div(
                Div(Submit('submit', 'Apply Filter'), css_class="col-sm-3"),
                css_class='row'),
            css_class='container')

    )


class ParkedCaneFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        Div(
            Div(
                Div('branch_of_origin', css_class="col-sm-3"),
                Div('date', css_class="col-sm-3"),
                css_class="row"
            ),
            Div(
                Div(Submit('submit', 'Apply Filter'), css_class="col-sm-3"),
                css_class='row'),
            css_class='container')

    )


class LoadersFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        Div(
            Div(
                Div('loader_name', css_class="col-sm-6"),
                css_class="row"
            ),
            Div(
                Div(Submit('submit', 'Apply Filter'), css_class="col-sm-3"),
                css_class='row'),
            css_class='container')

    )


class TowingFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        Div(
            Div(
                Div('branch_of_origin', css_class="col-sm-4"),
                css_class="row"
            ),
            Div(
                Div(Submit('submit', 'Apply Filter'), css_class="col-sm-3"),
                css_class='row'),
            css_class='container')

    )


class PickupsAndCanterControlFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        Div(
            Div(
                Div('driver', css_class="col-sm-4"),
                css_class="row"
            ),
            Div(
                Div(Submit('submit', 'Apply Filter'), css_class="col-sm-3"),
                css_class='row'),
            css_class='container')

    )


class TicketReconciliationFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        Div(
            Div(
                Div('ticket_trip', css_class="col-sm-4"),
                css_class="row"
            ),
            Div(
                Div(Submit('submit', 'Apply Filter'), css_class="col-sm-3"),
                css_class='row'),
            css_class='container')

    )


class TrailerAttachmentFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        Div(
            Div(
                Div('trailer', css_class="col-sm-4"),
                css_class="row"
            ),
            Div(
                Div(Submit('submit', 'Apply Filter'), css_class="col-sm-3"),
                css_class='row'),
            css_class='container')

    )


class DrivingLicenceValidityFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        Div(
            Div(
                Div('driver', css_class="col-sm-6"),
                css_class="row"
            ),
            Div(
                Div(Submit('submit', 'Apply Filter'), css_class="col-sm-3"),
                css_class='row'),
            css_class='container')

    )


class JournalEntryFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        Div(
            Div(
                Div('reference', css_class="col-sm-6"),
                css_class="row"
            ),
            Div(
                Div(Submit('submit', 'Apply Filter'), css_class="col-sm-3"),
                css_class='row'),
            css_class='container')

    )


class CustomerTransactionFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        Div(
            Div(
                Div('reference', css_class="col-sm-6"),
                css_class="row"
            ),
            Div(
                Div(Submit('submit', 'Apply Filter'), css_class="col-sm-3"),
                css_class='row'),
            css_class='container')

    )


class SupplierTransactionFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        Div(
            Div(
                Div('reference', css_class="col-sm-6"),
                css_class="row"
            ),
            Div(
                Div(Submit('submit', 'Apply Filter'), css_class="col-sm-3"),
                css_class='row'),
            css_class='container')

    )


class ReceivePaymentFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        Div(
            Div(
                Div('reference', css_class="col-sm-6"),
                css_class="row"
            ),
            Div(
                Div(Submit('submit', 'Apply Filter'), css_class="col-sm-3"),
                css_class='row'),
            css_class='container')

    )


class MakePaymentFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        Div(
            Div(
                Div('reference', css_class="col-sm-6"),
                css_class="row"
            ),
            Div(
                Div(Submit('submit', 'Apply Filter'), css_class="col-sm-3"),
                css_class='row'),
            css_class='container')

    )


class AttendanceFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        Div(
            Div(
                Div('name', css_class="col-sm-6"),
                css_class="row"
            ),
            Div(
                Div(Submit('submit', 'Apply Filter'), css_class="col-sm-3"),
                css_class='row'),
            css_class='container')

    )


class AllowancesDeductionsFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        Div(
            Div(
                Div('name', css_class="col-sm-6"),
                css_class="row"
            ),
            Div(
                Div(Submit('submit', 'Apply Filter'), css_class="col-sm-3"),
                css_class='row'),
            css_class='container')

    )


class HolidayPayFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        Div(
            Div(
                Div('name', css_class="col-sm-6"),
                css_class="row"
            ),
            Div(
                Div(Submit('submit', 'Apply Filter'), css_class="col-sm-3"),
                css_class='row'),
            css_class='container')

    )


class FuelReadingsFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        Div(
            Div(
                Div('fuel_pump', css_class="col-sm-3"),
                css_class="row"
            ),
            Div(
                Div(Submit('submit', 'Apply Filter'), css_class="col-sm-3"),
                css_class='row'),
            css_class='container')
    )


class StockArticleReceiptFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        Div(
            Div(
                Div('reference_no', css_class="col-sm-3"),
                css_class="row"
            ),
            Div(
                Div(Submit('submit', 'Apply Filter'), css_class="col-sm-3"),
                css_class='row'),
            css_class='container')
    )


class StockArticleIssueFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        Div(
            Div(
                Div('reference_no', css_class="col-sm-3"),
                css_class="row"
            ),
            Div(
                Div(Submit('submit', 'Apply Filter'), css_class="col-sm-3"),
                css_class='row'),
            css_class='container')
    )


class StockArticleAdjustmentFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        Div(
            Div(
                Div('reference_no', css_class="col-sm-3"),
                css_class="row"
            ),
            Div(
                Div(Submit('submit', 'Apply Filter'), css_class="col-sm-3"),
                css_class='row'),
            css_class='container')
    )


class FuelConsumptionFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        Div(
            Div(
                Div('driver', css_class="col-sm-3"),
                css_class="row"
            ),
            Div(
                Div(Submit('submit', 'Apply Filter'), css_class="col-sm-3"),
                css_class='row'),
            css_class='container')
    )


class InsuranceValidityFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        Div(
            Div(
                Div('insured_by', css_class="col-sm-6"),
                css_class="row"
            ),
            Div(
                Div(Submit('submit', 'Apply Filter'), css_class="col-sm-3"),
                css_class='row'),
            css_class='container')
    )
