from .models import (Designation, Department, Employee, TransportPayrollRate, PayrollCode, PayeBand,
                     NhifBand, Loader, Attendance, AllowanceAndDeductions, HolidayPay)
from .forms import (DesignationForm, DepartmentForm, EmployeeForm, TransportPayrollRateForm,
                    PayrollCodeForm, PayeBandForm, NhifBandForm, LoaderForm, AttendanceForm,
                    AllowanceAndDeductionsForm, HolidayPayForm)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.urls import reverse_lazy
from tenant.utilities import get_tenant
from django.views.generic.detail import DetailView
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    ListView,
    DeleteView,
    TemplateView
)


# Designation Views
# StockCategory Views
@login_required()
def designation_view(request):
    tenant = get_tenant(request)
    designations = Designation.objects.filter(tenant=tenant)

    return render(request, 'hr/designation.html', {'designations': designations, 'tenant': tenant})


@login_required()
def designation_create_view(request):
    form = DesignationForm()
    if request.method == 'POST':
        form = DesignationForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/hr/')
        else:
            form = DesignationForm()
    return render(request, 'hr/designation_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class DesignationUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'hr/designation_update.html'
    form_class = DesignationForm
    success_url = reverse_lazy('designation')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Designation, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class DesignationDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'hr/designation_delete.html'
    success_url = reverse_lazy('designation')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Designation, pk=pk_)


# Department View
@login_required()
def department_view(request):
    tenant = get_tenant(request)
    departments = Department.objects.filter(tenant=tenant)

    return render(request, 'hr/department.html', {'departments': departments, 'tenant': tenant})


@login_required()
def department_create_view(request):
    form = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/hr/department/')
        else:
            form = DepartmentForm()
    return render(request, 'hr/department_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'hr/department_update.html'
    form_class = DepartmentForm
    success_url = reverse_lazy('department')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Department, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'hr/department_delete.html'
    success_url = reverse_lazy('department')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Department, pk=pk_)


# Employee View
@login_required()
def employee_view(request):
    tenant = get_tenant(request)
    employees = Employee.objects.filter(tenant=tenant)

    return render(request, 'hr/employee.html', {'employees': employees, 'tenant': tenant})


@login_required()
def employee_create_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/hr/employee/')
        else:
            form = EmployeeForm()
    return render(request, 'hr/employee_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'hr/employee_update.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employee')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Employee, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'hr/employee_delete.html'
    success_url = reverse_lazy('employee')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Employee, pk=pk_)


# TransportPayrollRate View
@login_required()
def transport_payroll_view(request):
    tenant = get_tenant(request)
    transport_payroll = TransportPayrollRate.objects.filter(tenant=tenant)

    return render(request, 'hr/transport_payroll.html', {'transport_payroll': transport_payroll, 'tenant': tenant})


@login_required()
def transport_payroll_create_view(request):
    form = TransportPayrollRateForm()
    if request.method == 'POST':
        form = TransportPayrollRateForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/hr/transport_payroll/')
        else:
            form = TransportPayrollRateForm()
    return render(request, 'hr/transport_payroll_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class TransportPayrollUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'hr/transport_payroll_update.html'
    form_class = TransportPayrollRateForm
    success_url = reverse_lazy('transport_payroll')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(TransportPayrollRate, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class TransportPayrollDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'hr/transport_payroll_delete.html'
    success_url = reverse_lazy('transport_payroll')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(TransportPayrollRate, pk=pk_)


# PayrollCode View
@login_required()
def payroll_code_view(request):
    tenant = get_tenant(request)
    payrollcode = PayrollCode.objects.filter(tenant=tenant)

    return render(request, 'hr/payroll_code.html', {'payrollcode': payrollcode, 'tenant': tenant})


@login_required()
def payroll_code_create_view(request):
    form = PayrollCodeForm()
    if request.method == 'POST':
        form = PayrollCodeForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/hr/payroll_code/')
        else:
            form = PayrollCodeForm()
    return render(request, 'hr/payroll_code_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class PayrollCodeUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'hr/payroll_code_update.html'
    form_class = PayrollCodeForm
    success_url = reverse_lazy('payroll_code')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(PayrollCode, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class PayrollCodeDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'hr/payroll_code_delete.html'
    success_url = reverse_lazy('payroll_code')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(PayrollCode, pk=pk_)


# PayrollCode View
@login_required()
def paye_band_view(request):
    tenant = get_tenant(request)
    paye_bands = PayeBand.objects.filter(tenant=tenant)

    return render(request, 'hr/paye_band.html', {'paye_bands': paye_bands, 'tenant': tenant})


@login_required()
def paye_band_create_view(request):
    form = PayeBandForm()
    if request.method == 'POST':
        form = PayeBandForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/hr/paye_band/')
        else:
            form = PayeBandForm()
    return render(request, 'hr/paye_band_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class PayeBandUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'hr/paye_band_update.html'
    form_class = PayeBandForm
    success_url = reverse_lazy('paye_band_code')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(PayeBand, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class PayeBandDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'hr/paye_band_delete.html'
    success_url = reverse_lazy('paye_band')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(PayeBand, pk=pk_)


# PayrollCode View
@login_required()
def nhif_band_view(request):
    tenant = get_tenant(request)
    nhif_bands = NhifBand.objects.filter(tenant=tenant)

    return render(request, 'hr/nhif_band.html', {'nhif_bands': nhif_bands, 'tenant': tenant})


@login_required()
def nhif_band_create_view(request):
    form = NhifBandForm()
    if request.method == 'POST':
        form = NhifBandForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/hr/nhif_band/')
        else:
            form = NhifBandForm()
    return render(request, 'hr/nhif_band_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class NhifBandUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'hr/nhif_band_update.html'
    form_class = NhifBandForm
    success_url = reverse_lazy('nhif_band')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(NhifBand, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class NhifBandDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'hr/nhif_band_delete.html'
    success_url = reverse_lazy('nhif_band')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(NhifBand, pk=pk_)


# PayrollCode View
@login_required()
def loader_view(request):
    tenant = get_tenant(request)
    loaders = Loader.objects.filter(tenant=tenant)

    return render(request, 'hr/loader.html', {'loaders': loaders, 'tenant': tenant})


@login_required()
def loader_create_view(request):
    form = LoaderForm()
    if request.method == 'POST':
        form = LoaderForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/hr/loader/')
        else:
            form = LoaderForm()
    return render(request, 'hr/loader_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class LoaderUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'hr/loader_update.html'
    form_class = LoaderForm
    success_url = reverse_lazy('loader')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Loader, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class LoaderDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'hr/loader_delete.html'
    success_url = reverse_lazy('loader')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Loader, pk=pk_)


@login_required()
def attendance_view(request):
    tenant = get_tenant(request)
    attendance = Attendance.objects.filter(tenant=tenant)

    return render(request, 'hr/attendance.html', {'attendance': attendance, 'tenant': tenant})


@login_required()
def attendance_create_view(request):
    form = AttendanceForm()
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/hr/attendance/')
        else:
            form = AttendanceForm()
    return render(request, 'hr/attendance_create.html', {'form': form})


@login_required()
def allowancesDeductions_view(request):
    tenant = get_tenant(request)
    allowancesDeductions = AllowanceAndDeductions.objects.filter(tenant=tenant)

    return render(request, 'hr/allowances_deductions.html',
                  {'allowancesDeductions': allowancesDeductions, 'tenant': tenant})


@login_required()
def allowancesDeductions_create_view(request):
    form = AllowanceAndDeductionsForm()
    if request.method == 'POST':
        form = AllowanceAndDeductionsForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/hr/allowancesDeductions/')
        else:
            form = AllowancesDeductionsForm()
    return render(request, 'hr/allowances_deductions_create.html', {'form': form})


@login_required()
def holidayPay_view(request):
    tenant = get_tenant(request)
    holidayPays = HolidayPay.objects.filter(tenant=tenant)
    total_amount = sum(holidayPays.values_list('amount', flat=True))

    return render(request, 'hr/holidayPay.html',
                  {'holidayPays': holidayPays, 'total_amount': total_amount, 'tenant': tenant})


@login_required()
def holidayPay_create_view(request):
    form = HolidayPayForm()
    if request.method == 'POST':
        form = HolidayPayForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/hr/holidayPay/')
        else:
            form = HolidayPayForm()
    return render(request, 'hr/holidayPay_create.html', {'form': form})
