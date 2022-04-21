from django.urls import path, include
from .views import (designation_view, designation_create_view, DesignationUpdateView, DesignationDeleteView,
                    department_view, department_create_view, DepartmentUpdateView, DepartmentDeleteView,
                    employee_view, employee_create_view, EmployeeUpdateView, EmployeeDeleteView,
                    transport_payroll_view, transport_payroll_create_view, TransportPayrollUpdateView, TransportPayrollDeleteView,
                    payroll_code_view, payroll_code_create_view, PayrollCodeUpdateView, PayrollCodeDeleteView,
                    paye_band_view, paye_band_create_view, PayeBandUpdateView, PayeBandDeleteView,
                    nhif_band_view, nhif_band_create_view, NhifBandUpdateView, NhifBandDeleteView,
                    loader_view, loader_create_view, LoaderUpdateView, LoaderDeleteView,attendance_view,attendance_create_view,
                    allowancesDeductions_view, allowancesDeductions_create_view,holidayPay_view,holidayPay_create_view)


urlpatterns = [
    #Designation url
    path('', designation_view, name="designation"),
    path('designation_create/',designation_create_view, name = 'designation_create'),
    path('<pk>/designation_update/', DesignationUpdateView.as_view(), name = 'designation_update'),
    path('<pk>/designation_delete/',DesignationDeleteView.as_view(), name = 'designation_delete'),
    #Department urls
    path('department/', department_view, name="department"),
    path('department_create/', department_create_view, name='department_create'),
    path('department/<pk>/department_update/', DepartmentUpdateView.as_view(), name='department_update'),
    path('department/<pk>/department_delete/', DepartmentDeleteView.as_view(), name='department_delete'),
    #Employee urls
    path('employee/', employee_view, name="employee"),
    path('employee_create/',employee_create_view, name = 'employee_create'),
    path('employee/<pk>/employee_update/', EmployeeUpdateView.as_view(), name = 'employee_update'),
    path('employee/<pk>/employee_delete/',EmployeeDeleteView.as_view(), name = 'employee_delete'),
    #Transport Payroll Codes url
    path('transport_payroll/', transport_payroll_view, name="transport_payroll"),
    path('transport_payroll_create/',transport_payroll_create_view, name = 'transport_payroll_create'),
    path('transport_payroll/<pk>/transport_payroll_update/', TransportPayrollUpdateView.as_view(), name = 'transport_payroll_update'),
    path('transport_payroll/<pk>/transport_payroll_delete/',TransportPayrollDeleteView.as_view(), name = 'transport_payroll_delete'),
    #Payroll Code urls
    path('payroll_code/', payroll_code_view, name="payroll_code"),
    path('payroll_code_create/', payroll_code_create_view, name='payroll_code_create'),
    path('payroll_code/<pk>/payroll_code_update/', PayrollCodeUpdateView.as_view(), name='payroll_code_update'),
    path('payroll_code/<pk>/payroll_code_delete/', PayrollCodeDeleteView.as_view(), name='payroll_code_delete'),
    #Paye Bands urls
    path('paye_band/', paye_band_view, name="paye_band"),
    path('paye_band_create/',paye_band_create_view, name = 'paye_band_create'),
    path('paye_band/<pk>/paye_band_update/', PayeBandUpdateView.as_view(), name = 'paye_band_update'),
    path('paye_band/<pk>/paye_band_delete/',PayeBandDeleteView.as_view(), name = 'paye_band_delete'),
    #NHIF band urls
    path('nhif_band/', nhif_band_view, name="nhif_band"),
    path('nhif_band_create/', nhif_band_create_view, name='nhif_band_create'),
    path('nhif_band/<pk>/nhif_band_update/', NhifBandUpdateView.as_view(), name='nhif_band_update'),
    path('nhif_band/<pk>/nhif_band_delete/', NhifBandDeleteView.as_view(), name='nhif_band_delete'),
    #Loaders urls
    path('loader/', loader_view, name="loader"),
    path('loader_create/', loader_create_view, name='loader_create'),
    path('loader/<pk>/loader_update/', LoaderUpdateView.as_view(), name='loader_update'),
    path('loader/<pk>/loader_delete/', LoaderDeleteView.as_view(), name='loader_delete'),
    #Attendance
    path('attendance/',attendance_view, name="attendance"),
    path('attendance_create/',attendance_create_view, name="attendance_create"),
    #AllowancesAndDeductions
    path('allowancesDeductions/',allowancesDeductions_view, name="allowancesDeductions"),
    path('allowancesDeductions_create/',allowancesDeductions_create_view, name="allowancesDeductions_create"),
    #HolidayPay
    path('holidayPay/',holidayPay_view, name="holidayPay"),
    path('holidayPay_create/',holidayPay_create_view, name="holidayPay_create")

]

