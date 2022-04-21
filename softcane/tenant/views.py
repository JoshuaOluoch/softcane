from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.urls import reverse_lazy
from .models import VehicleType, Vehicle
from .utilities import get_tenant

from users.models import User
from django.contrib import messages

from .forms import VehicleTypeForm, VehicleForm, VehicleTypeEditForm
from django.views.generic.detail import DetailView
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    ListView,
    DeleteView,
    TemplateView
)


# Vehicle type views
@login_required()
def our_vehicle_type(request):
    tenant = get_tenant(request)
    vehicle_types = VehicleType.objects.filter(tenant=tenant)

    return render(request, 'tenant/our_vehicle_types.html', {'vehicle_types': vehicle_types, 'tenant': tenant})


@login_required()
def vehicle_type_create(request):
    form = VehicleTypeForm()
    if request.method == 'POST':
        form = VehicleTypeForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/configuration_vehicle_type/')
        else:
            form = VehicleTypeForm()
    return render(request, 'tenant/create_vehicle_type.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class VehicleTypeUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'tenant/vehicle_type_update.html'
    form_class = VehicleTypeForm
    success_url = reverse_lazy('vehicle-types')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(VehicleType, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class VehicleTypeDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'tenant/vehicle_type_delete.html'
    success_url = reverse_lazy('vehicle-types')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(VehicleType, pk=pk_)


## Vehicle Views
@login_required()
def vehicle(request):
    tenant = get_tenant(request)
    vehicles = Vehicle.objects.filter(tenant=tenant)

    return render(request, 'tenant/vehicles.html', {'vehicles': vehicles, 'tenant': tenant})


@login_required()
def vehicle_create(request):
    form = VehicleForm()
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/vehicle/')
        else:
            form = VehicleForm()
    return render(request, 'tenant/vehicle_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'tenant/vehicle_update.html'
    form_class = VehicleForm
    success_url = reverse_lazy('vehicle')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Vehicle, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'tenant/vehicle_delete.html'
    success_url = reverse_lazy('vehicle')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Vehicle, pk=pk_)


def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            return redirect('change_password')
    else:
        return render(request, 'users/forgot_password.html')


def changePassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            user = User.objects.get(request.user)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password Reset Successfully')
            return redirect('login')
        else:
            messages.error(request, 'Password do not match!')
            return redirect('change_password')
    return render(request, 'users/resetPassword.html')
