import django_tables2 as tables
from transport.models import *
from accounting.models import *
from hr.models import *
from stock.models import *
from django.db.models import Sum


class TripTable(tables.Table):
    trip_branch = tables.Column(footer="Total:")

    class Meta:
        model = Trip
        sequence = ("trip_branch", "ticket_number", "tractor_or_lorry", "weight_in", "weight_out", "net_weight",)
        exclude = ("trip_id", "trip_number", "trip_zone", "trip_sub_location", "trip_field", "trip_date", "trip_driver",
                   "field_in",
                   "field_out", "field_net", "loaded_by_1", "loading_driver_1", "loaded_by_2", "loading_driver_2",
                   "time_in", "time_out",
                   "trip_type", 'id', 'tenant', 'posted_by', 'posted_date', 'tenantawaremodel_ptr')
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",
                    "ascending": "ascend",
                    "descending": "descend"
                }
            }
        }


class ParkedCaneTable(tables.Table):
    branch_of_origin = tables.Column(footer="Total:")

    class Meta:
        model = PackedCane
        sequence = ("branch_of_origin", "trip_zone", "trip_sub_location", "trip_field", "tractor", "stacks")
        exclude = (
            "packed_cane_id", "delivery_note", "date", "loaded_by_1", "loading_driver_1", "loaded_by_2",
            "loading_driver_2",
            "posted_by", "posted_date", "tenantawaremodel_ptr", 'id', 'tenant',)
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",
                    "ascending": "ascend",
                    "descending": "descend"
                }
            }
        }


class LoadersTable(tables.Table):
    class Meta:
        model = LoadersDailyEntry
        sequence = ("loader_name", "worked", "date")
        exclude = (
            "loaders_daily_entry_id", "posted_by", "posted_date", "tenantawaremodel_ptr", 'id', 'tenant',)
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",
                    "ascending": "ascend",
                    "descending": "descend"
                }
            }
        }


class TowingTable(tables.Table):
    branch_of_origin = tables.Column(footer="Total:")

    class Meta:
        model = Towing
        sequence = ("branch_of_origin", "driver", "winch", "number_of_tows", "date")
        exclude = (
            "towing_id", "posted_by", "posted_date", "tenantawaremodel_ptr", 'id', 'tenant',)
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",
                    "ascending": "ascend",
                    "descending": "descend"
                }
            }
        }


class PickupsAndCanterControlTable(tables.Table):
    class Meta:
        model = PickupsAndCantersControl
        sequence = ("driver", "vehicle_name", "opening_reading", "closing_reading", "milage", "date")
        exclude = (
            "pickup_canter_control_id", "posted_by", "posted_date", "tenantawaremodel_ptr", 'id', 'tenant',)
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",
                    "ascending": "ascend",
                    "descending": "descend"
                }
            }
        }


class TicketReconciliationTable(tables.Table):
    class Meta:
        model = TicketReconciliation
        sequence = ("ticket_trip", "paid")
        exclude = (
            "ticket_reconciliation_id", "posted_by", "posted_date", "tenantawaremodel_ptr", 'id', 'tenant',)
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",
                    "ascending": "ascend",
                    "descending": "descend"
                }
            }
        }


class TrailerAttachmentTable(tables.Table):
    class Meta:
        model = TrailerAttachment
        sequence = ("trailer", "tractor", "date")
        exclude = (
            "trailer_attachment_id", "posted_by", "posted_date", "tenantawaremodel_ptr", 'id', 'tenant',)
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",
                    "ascending": "ascend",
                    "descending": "descend"
                }
            }
        }


class DrivingLicenceValidityTable(tables.Table):
    class Meta:
        model = DrivingLicenceValidity
        sequence = ("driver", "licence_no", "expiry_date")
        exclude = (
            "licence_id", "active_date", "posted_by", "posted_date", "tenantawaremodel_ptr", 'id', 'tenant',)
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",
                    "ascending": "ascend",
                    "descending": "descend"
                }
            }
        }


class JournalEntryTable(tables.Table):
    transaction_no = tables.Column(footer="Total:")

    class Meta:
        model = JournalEntry
        sequence = (
            "transaction_no", "debit_account", "reference", "amount", "narration", "credit_account", "posted_by",
            "posted_date")
        exclude = (
            "journal_entry_id", "tenantawaremodel_ptr", "id", "tenant", "tenant_customer_id", "customer_vat_number",
            "customer_pin_number", "customer_email", "customer_telephone", "customer_postal_code", "customer_name",
            "date", "tenantcustomer_ptr"
        )
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",
                    "ascending": "ascend",
                    "descending": "descend"
                }
            }
        }


class CustomerTransactionTable(tables.Table):
    customer = tables.Column(footer="Total:")

    class Meta:
        model = CustomerTransaction
        sequence = (
            "customer", "transaction_no", "transaction_type", "reference", "amount", "narration", "posted_by",
            "gl_account", "posted_date")
        exclude = (
            "customer_transaction_id", "tenantawaremodel_ptr", "id", "tenant", "tenant_customer_id",
            "customer_vat_number",
            "customer_pin_number", "customer_email", "customer_telephone", "customer_postal_code", "customer_name",
            "date", "tenantcustomer_ptr"
        )
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",
                    "ascending": "ascend",
                    "descending": "descend"
                }
            }
        }


class SupplierTransactionTable(tables.Table):
    supplier = tables.Column(footer="Total:")

    class Meta:
        model = SupplierTransaction
        sequence = (
            "supplier", "transaction_no", "transaction_type", "reference", "amount", "narration", "posted_by",
            "gl_account", "posted_date")
        exclude = (
            "supplier_customer_id", "customer_transaction_id", "tenantawaremodel_ptr", "id", "tenant",
            "tenant_customer_id", "supplier_vat_number", "supplier_pin_number", "supplier_email", "supplier_telephone",
            "supplier_postal_code", "supplier_name", "date", "tenantcustomer_ptr"
        )
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",
                    "ascending": "ascend",
                    "descending": "descend"
                }
            }
        }


class ReceivePaymentTable(tables.Table):
    received_from = tables.Column(footer="Total:")

    class Meta:
        model = ReceivePayment
        sequence = (
            "received_from", "transaction_no", "reference", "amount", "narration", "posted_by", "posted_date")
        exclude = (
            "received_payment_id", "tenantawaremodel_ptr", "id", "tenant", "tenant_customer_id",
            "customer_vat_number",
            "customer_pin_number", "customer_email", "customer_telephone", "customer_postal_code", "customer_name",
            "date", "tenantcustomer_ptr"
        )
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",
                    "ascending": "ascend",
                    "descending": "descend"
                }
            }
        }


class MakePaymentTable(tables.Table):
    paid_to = tables.Column(footer="Total:")

    class Meta:
        model = MakePayment
        sequence = (
            "paid_to", "supplier_account", "transaction_no", "reference", "amount", "narration", "date", "posted_by",
            "posted_date")
        exclude = (
            "make_payment_id", "customer_transaction_id", "tenantawaremodel_ptr", "id", "tenant",
            "tenant_customer_id", "supplier_vat_number", "supplier_pin_number", "supplier_email", "supplier_telephone",
            "supplier_postal_code", "supplier_name", "tenantcustomer_ptr"
        )
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",
                    "ascending": "ascend",
                    "descending": "descend"
                }
            }
        }


class AttendanceTable(tables.Table):
    class Meta:
        model = Attendance
        sequence = (
            "name", "department_category", "attend", "date",)
        exclude = (
            "attendance_id", "tenantawaremodel_ptr", "id", "tenant", "tenant_customer_id", "tenantcustomer_ptr"
        )
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",
                    "ascending": "ascend",
                    "descending": "descend"
                }
            }
        }


class AllowancesDeductionsTable(tables.Table):
    name = tables.Column(footer="Total:")

    class Meta:
        model = AllowanceAndDeductions
        sequence = (
            "name", "trans_code", "desc", "amount", "date",)
        exclude = (

            "allowance_id", "attendance_id", "tenantawaremodel_ptr", "id", "tenant", "tenant_customer_id",
            "tenantcustomer_ptr"
        )
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",
                    "ascending": "ascend",
                    "descending": "descend"
                }
            }
        }


class HolidayPayTable(tables.Table):
    name = tables.Column(footer="Total:")

    class Meta:
        model = HolidayPay
        sequence = (
            "name", "trans_code", "amount", "date",)
        exclude = (

            "holidaypay_id", "tenantawaremodel_ptr", "id", "tenant", "tenant_customer_id", "tenantcustomer_ptr"
        )
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",
                    "ascending": "ascend",
                    "descending": "descend"
                }
            }
        }


class FuelReadingsTable(tables.Table):
    fuel_pump = tables.Column(footer="Total:")

    class Meta:
        model = FuelReadings
        sequence = (
            "fuel_pump", "morning_tank_dipping", "morning_pump_reading", "evening_tank_dipping", "evening_pump_reading",
            "date")
        exclude = (

            "fuel_readings_id", "tenantawaremodel_ptr", "id", "tenant", "tenant_customer_id", "tenantcustomer_ptr"
        )
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",
                    "ascending": "ascend",
                    "descending": "descend"
                }
            }
        }


class StockArticleReceiptTable(tables.Table):
    transaction_no = tables.Column(footer="Total:")

    class Meta:
        model = StockArticleReceipt
        sequence = (
            "transaction_no", "type", "reference_no", "supplier_account", "item", "item_category", "part_number",
            "quantity_received", "unit_cost", "remark", "posted_by", "posted_date", "date")
        exclude = (

            "stock_article_receipt_id", "tenantawaremodel_ptr", "id", "tenant", "tenant_customer_id",
            "tenantcustomer_ptr"
        )
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",
                    "ascending": "ascend",
                    "descending": "descend"
                }
            }
        }


class StockArticleIssueTable(tables.Table):
    transaction_no = tables.Column(footer="Total:")

    class Meta:
        model = StockArticleIssue
        sequence = (
            "transaction_no", "type", "reference_no", "customer", "item", "item_category", "part_number",
            "quantity_received", "unit_cost", "remark", "posted_by", "posted_date", "date")
        exclude = (

            "stock_article_issue_id", "tenantawaremodel_ptr", "id", "tenant", "tenant_customer_id", "tenantcustomer_ptr"
        )
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",
                    "ascending": "ascend",
                    "descending": "descend"
                }
            }
        }


class StockArticleAdjustmentTable(tables.Table):
    transaction_no = tables.Column(footer="Total:")

    class Meta:
        model = StockArticleAdjustment
        sequence = (
            "transaction_no", "type", "reference_no", "item", "item_category", "part_number",
            "required_quantity", "current_quantity", "remark", "posted_by", "posted_date", "date")
        exclude = (

            "stock_article_adjustment_id", "tenantawaremodel_ptr", "id", "tenant", "tenant_customer_id",
            "tenantcustomer_ptr"
        )
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",
                    "ascending": "ascend",
                    "descending": "descend"
                }
            }
        }


class FuelConsumptionTable(tables.Table):
    driver = tables.Column(footer="Total:")

    class Meta:
        model = FuelConsumption
        sequence = (
            "driver", "vehicle_fueled", "quantity_in_litres", "branch_of_origin", "posted_by", "posted_date", "date")
        exclude = (

            "fuel_consumption_id", "tenantawaremodel_ptr", "id", "tenant", "tenant_customer_id", "tenantcustomer_ptr"
        )
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",
                    "ascending": "ascend",
                    "descending": "descend"
                }
            }
        }


class InsuranceValidityTable(tables.Table):
    class Meta:
        model = InsuranceValidity
        sequence = (
            "certificate_number", "vehicle_name", "policy_no", "policy_type", "commence_date", "expiry_date",
            "delivery_note_no", "risk_covered", "insured_by")
        exclude = (

            "insurance_validity_id", "tenantawaremodel_ptr", "id", "tenant", "tenant_customer_id", "tenantcustomer_ptr"
        )
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",
                    "ascending": "ascend",
                    "descending": "descend"
                }
            }
        }
