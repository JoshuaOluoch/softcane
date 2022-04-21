from .models import (TransportInfo, Trip, FuelConsumption, Towing, PackedCane, LoadersDailyEntry,
                     PickupsAndCantersControl,
                     TicketReconciliation, TrailerAttachment, InsuranceRisk, InsuranceCompany, InsuranceValidity,
                     DrivingLicenceValidity)
from .forms import (TransportInfoForm, TripForm, FuelConsumptionForm, TowingForm, PackedCaneForm, LoadersDailyEntryForm,
                    PickupsAndCantersControlForm, TicketReconciliationForm, TrailerAttachmentForm, InsuranceRiskForm,
                    InsuranceCompanyForm, InsuranceValidityForm, DrivingLicenceValidityForm)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.urls import reverse_lazy
from tenant.utilities import get_tenant
from django.template import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    ListView,
    DeleteView,
    TemplateView
)


@login_required()
def transport_info_view(request):
    tenant = get_tenant(request)
    transport_infos = TransportInfo.objects.filter(tenant=tenant)

    return render(request, 'transport/transport_info.html', {'transport_infos': transport_infos, 'tenant': tenant})


@login_required()
def transport_info_create_view(request):
    form = TransportInfoForm()
    if request.method == 'POST':
        form = TransportInfoForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.instance.posted_by = request.user
            form.save(commit=True)
            return redirect('/transport/')
        else:
            form = TransportInfoForm()
    return render(request, 'transport/transport_info_create.html', {'form': form})


class TransportInfoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/transport_info_update.html'
    form_class = TransportInfoForm
    success_url = reverse_lazy('transport_info')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(TransportInfo, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class TransportInfoDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/transport_info_delete.html'
    success_url = reverse_lazy('transport_info')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(TransportInfo, pk=pk_)


# Trip views
@login_required()
def trip_view(request):
    tenant = get_tenant(request)
    trips = Trip.objects.filter(tenant=tenant)

    return render(request, 'transport/trip.html', {'trips': trips, 'tenant': tenant})


@login_required()
def trip_create_view(request):
    form = TripForm()
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.instance.posted_by = request.user
            form.instance.net_weight = form.instance.weight_in - form.instance.weight_out
            form.instance.field_net = form.instance.field_in - form.instance.field_out
            form.save(commit=True)
            return redirect('/transport/trip/')
        else:
            form = TripForm()
    return render(request, 'transport/trip_create.html', {'form': form})


class TripUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/trip_update.html'
    form_class = TripForm
    success_url = reverse_lazy('trip')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Trip, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class TripDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/trip_delete.html'
    success_url = reverse_lazy('trip')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Trip, pk=pk_)


# Fuel consumption Views
@login_required()
def fuel_consumption_view(request):
    tenant = get_tenant(request)
    fuel_consumption = FuelConsumption.objects.filter(tenant=tenant)

    return render(request, 'transport/fuel_consumption.html', {'fuel_consumption': fuel_consumption, 'tenant': tenant})


@login_required()
def fuel_consumption_create_view(request):
    form = FuelConsumptionForm()
    if request.method == 'POST':
        form = FuelConsumptionForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.instance.posted_by = request.user
            form.save(commit=True)
            return redirect('/transport/fuel_consumption/')
        else:
            form = FuelConsumptionForm()
    return render(request, 'transport/fuel_consumption_create.html', {'form': form})


class FuelConsumptionUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/fuel_consumption_update.html'
    form_class = FuelConsumptionForm
    success_url = reverse_lazy('fuel_consumption')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(FuelConsumption, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class FuelConsumptionDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/fuel_consumption_delete.html'
    success_url = reverse_lazy('fuel_consumption')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(FuelConsumption, pk=pk_)


# TowingForm Views
@login_required()
def towing_view(request):
    tenant = get_tenant(request)
    towings = Towing.objects.filter(tenant=tenant)

    return render(request, 'transport/towing.html', {'towings': towings, 'tenant': tenant})


@login_required()
def towing_create_view(request):
    form = TowingForm()
    if request.method == 'POST':
        form = TowingForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.instance.posted_by = request.user
            form.save(commit=True)
            return redirect('/transport/towing/')
        else:
            form = TowingForm()
    return render(request, 'transport/towing_create.html', {'form': form})


class TowingUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/towing_update.html'
    form_class = TowingForm
    success_url = reverse_lazy('towing')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Towing, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class TowingDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/towing_delete.html'
    success_url = reverse_lazy('towing')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Towing, pk=pk_)


# PackedCane Views
@login_required()
def packed_cane_view(request):
    tenant = get_tenant(request)
    packed_cane = PackedCane.objects.filter(tenant=tenant)

    return render(request, 'transport/packed_cane.html', {'packed_cane': packed_cane, 'tenant': tenant})


@login_required()
def packed_cane_create_view(request):
    form = PackedCaneForm()
    if request.method == 'POST':
        form = PackedCaneForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.instance.posted_by = request.user
            form.save(commit=True)
            return redirect('/transport/packed_cane/')
        else:
            form = PackedCaneForm()
    return render(request, 'transport/packed_cane_create.html', {'form': form})


class PackedCaneUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/packed_cane_update.html'
    form_class = PackedCaneForm
    success_url = reverse_lazy('packed_cane')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(PackedCane, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class PackedCaneDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/packed_cane_delete.html'
    success_url = reverse_lazy('packed_cane')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(PackedCane, pk=pk_)


# LoadersDailyEntry Views
@login_required()
def loaders_entry_view(request):
    tenant = get_tenant(request)
    loaders_entries = LoadersDailyEntry.objects.filter(tenant=tenant)

    return render(request, 'transport/loaders_entry.html', {'loaders_entries': loaders_entries, 'tenant': tenant})


@login_required()
def loaders_entry_create_view(request):
    form = LoadersDailyEntryForm()
    if request.method == 'POST':
        form = LoadersDailyEntryForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.instance.posted_by = request.user
            form.save(commit=True)
            return redirect('/transport/loaders_entry/')
        else:
            form = LoadersDailyEntryForm()
    return render(request, 'transport/loaders_entry_create.html', {'form': form})


class LoadersDailyEntryUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/loaders_entry_update.html'
    form_class = LoadersDailyEntryForm
    success_url = reverse_lazy('loaders_entry')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(LoadersDailyEntry, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class LoadersDailyEntryDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/loaders_entry_delete.html'
    success_url = reverse_lazy('loaders_entry')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(LoadersDailyEntry, pk=pk_)


# PickupsAndCantersControl Views
@login_required()
def pickup_canter_control_view(request):
    tenant = get_tenant(request)
    pickup_canter_control = PickupsAndCantersControl.objects.filter(tenant=tenant)

    return render(request, 'transport/pickup_canter_control.html',
                  {'pickup_canter_control': pickup_canter_control, 'tenant': tenant})


@login_required()
def pickup_canter_control_create_view(request):
    form = PickupsAndCantersControlForm()
    if request.method == 'POST':
        form = PickupsAndCantersControlForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.instance.posted_by = request.user
            form.save(commit=True)
            return redirect('/transport/pickup_canter_control/')
        else:
            form = PickupsAndCantersControlForm()
    return render(request, 'transport/pickup_canter_control_create.html', {'form': form})


class PickupsAndCantersControlUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/pickup_canter_control_update.html'
    form_class = PickupsAndCantersControlForm
    success_url = reverse_lazy('pickup_canter_control')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(PickupsAndCantersControl, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class PickupsAndCantersControlDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/pickup_canter_control_delete.html'
    success_url = reverse_lazy('pickup_canter_control')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(PickupsAndCantersControl, pk=pk_)


# TicketReconciliation Views
@login_required()
def ticket_reconciliation_view(request):
    tenant = get_tenant(request)
    ticket_reconciliation = TicketReconciliation.objects.filter(tenant=tenant)

    return render(request, 'transport/ticket_reconciliation.html',
                  {'ticket_reconciliation': ticket_reconciliation, 'tenant': tenant})


@login_required()
def ticket_reconciliation_create_view(request):
    form = TicketReconciliationForm()
    if request.method == 'POST':
        form = TicketReconciliationForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.instance.posted_by = request.user
            form.save(commit=True)
            return redirect('/transport/ticket_reconciliation/')
        else:
            form = TicketReconciliationForm()
    return render(request, 'transport/ticket_reconciliation_create.html', {'form': form})


class TicketReconciliationUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/ticket_reconciliation_update.html'
    form_class = TicketReconciliationForm
    success_url = reverse_lazy('ticket_reconciliation')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(TicketReconciliation, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class TicketReconciliationDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/ticket_reconciliation_delete.html'
    success_url = reverse_lazy('ticket_reconciliation')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(TicketReconciliation, pk=pk_)


# TrailerAttachment Views
@login_required()
def trailer_attachment_view(request):
    tenant = get_tenant(request)
    trailer_attachment = TrailerAttachment.objects.filter(tenant=tenant)

    return render(request, 'transport/trailer_attachment.html',
                  {'trailer_attachment': trailer_attachment, 'tenant': tenant})


@login_required()
def trailer_attachment_create_view(request):
    form = TrailerAttachmentForm()
    if request.method == 'POST':
        form = TrailerAttachmentForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.instance.posted_by = request.user
            form.save(commit=True)
            return redirect('/transport/trailer_attachment/')
        else:
            form = TrailerAttachmentForm()
    return render(request, 'transport/trailer_attachment_create.html', {'form': form})


class TrailerAttachmentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/trailer_attachment_update.html'
    form_class = TrailerAttachmentForm
    success_url = reverse_lazy('trailer_attachment')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(TrailerAttachment, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class TrailerAttachmentDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/trailer_attachment_delete.html'
    success_url = reverse_lazy('trailer_attachment')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(TrailerAttachment, pk=pk_)


# Insurance Validity Views
@login_required()
def insurance_validity_view(request):
    tenant = get_tenant(request)
    insurance_risks = InsuranceRisk.objects.filter(tenant=tenant)
    insurance_companies = InsuranceCompany.objects.filter(tenant=tenant)
    insurance_validity = InsuranceValidity.objects.filter(tenant=tenant)

    return render(request,
                  'transport/insurance_validity.html',
                  {'insurance_risks': insurance_risks, 'insurance_companies': insurance_companies,
                   'insurance_validity': insurance_validity, 'tenant': tenant})


@login_required()
def insurance_risk_create_view(request):
    form = InsuranceRiskForm()
    if request.method == 'POST':
        form = InsuranceRiskForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/transport/insurance_validity/')
        else:
            form = InsuranceRiskForm()
    return render(request, 'transport/insurance_risk_create.html', {'form': form})


@login_required()
def insurance_company_create_view(request):
    form = InsuranceCompanyForm()
    if request.method == 'POST':
        form = InsuranceCompanyForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/transport/insurance_validity/')
        else:
            form = InsuranceCompanyForm()
    return render(request, 'transport/insurance_company_create.html', {'form': form})


@login_required()
def insurance_validity_create_view(request):
    form = InsuranceValidityForm()
    if request.method == 'POST':
        form = InsuranceValidityForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/transport/insurance_validity/')
        else:
            form = InsuranceValidityForm()
    return render(request, 'transport/insurance_validity_create.html', {'form': form})


class InsuranceRiskUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/insurance_risk_update.html'
    form_class = InsuranceRiskForm
    success_url = reverse_lazy('insurance_validity')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(InsuranceRisk, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class InsuranceRiskDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/insurance_risk_delete.html'
    success_url = reverse_lazy('insurance_validity')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(InsuranceRisk, pk=pk_)


class InsuranceCompanyUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/insurance_company_update.html'
    form_class = InsuranceCompanyForm
    success_url = reverse_lazy('insurance_validity')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(InsuranceCompany, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class InsuranceCompanyDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/insurance_company_delete.html'
    success_url = reverse_lazy('insurance_validity')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(InsuranceCompany, pk=pk_)


class InsuranceValidityUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/insurance_validity_update.html'
    form_class = InsuranceValidityForm
    success_url = reverse_lazy('insurance_validity')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(InsuranceCompany, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class InsuranceValidityDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/insurance_validity_delete.html'
    success_url = reverse_lazy('insurance_validity')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(InsuranceValidity, pk=pk_)


# DrivingLicenceValidity Views
@login_required()
def driving_licence_validity_view(request):
    tenant = get_tenant(request)
    driving_licence_validity = DrivingLicenceValidity.objects.filter(tenant=tenant)

    return render(request, 'transport/driving_licence_validity.html',
                  {'driving_licence_validity': driving_licence_validity, 'tenant': tenant})


@login_required()
def driving_licence_validity_create_view(request):
    form = DrivingLicenceValidityForm()
    if request.method == 'POST':
        form = DrivingLicenceValidityForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/transport/driving_licence_validity/')
        else:
            form = DrivingLicenceValidityForm()
    return render(request, 'transport/driving_licence_validity_create.html', {'form': form})


class DrivingLicenceValidityUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/driving_licence_validity_update.html'
    form_class = DrivingLicenceValidityForm
    success_url = reverse_lazy('driving_licence_validity')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(DrivingLicenceValidity, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class DrivingLicenceValidityDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'transport/driving_licence_validity_delete.html'
    success_url = reverse_lazy('driving_licence_validity')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(DrivingLicenceValidity, pk=pk_)
