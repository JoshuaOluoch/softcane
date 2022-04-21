from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.urls import reverse_lazy
from .models import Branch,Zone, SubLocation, Field
from tenant.utilities import get_tenant
from .forms import BranchForm,ZoneForm, SubLocationForm,FieldForm
from django.views.generic.detail import DetailView
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    ListView,
    DeleteView,
    TemplateView
)
#Branch Viewa
@login_required()
def branch_view(request):
    tenant = get_tenant(request)
    branch = Branch.objects.filter(tenant=tenant)

    return render(request, 'location/branch.html',{'branch':branch, 'tenant':tenant})

@login_required()
def branch_create_view(request):
    form = BranchForm()
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/location/branch/')
        else:
            form = BranchForm()
    return render(request, 'location/branch_create.html', {'form' : form})

#class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class BranchUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'location/branch_update.html'
    form_class = BranchForm
    success_url = reverse_lazy('branch')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Branch, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)

class BranchDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'location/branch_delete.html'
    success_url = reverse_lazy('branch')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Branch, pk=pk_)

#Zone Views
@login_required()
def zone_view(request):
    tenant = get_tenant(request)
    zones = Zone.objects.filter(tenant=tenant)

    return render(request, 'location/zone.html',{'zones':zones, 'tenant':tenant})

@login_required()
def zone_create_view(request):
    form = ZoneForm()
    if request.method == 'POST':
        form = ZoneForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/location/')
        else:
            form = ZoneForm()
    return render(request, 'location/zone_create.html', {'form' : form})

#class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class ZoneUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'location/zone_update.html'
    form_class = ZoneForm
    success_url = reverse_lazy('zones')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Zone, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)

class ZoneDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'location/zone_delete.html'
    success_url = reverse_lazy('zones')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Zone, pk=pk_)

#SubLocation Views
@login_required()
def sub_location_view(request):
    tenant = get_tenant(request)
    sublocations = SubLocation.objects.filter(tenant=tenant)

    return render(request, 'location/sublocation.html',{'sublocations':sublocations, 'tenant':tenant})

@login_required()
def sub_location_create_view(request):
    form = SubLocationForm()
    if request.method == 'POST':
        form = SubLocationForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/location/sublocation/')
        else:
            form = SubLocationForm()
    return render(request, 'location/sublocation_create.html', {'form' : form})

#class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class SubLocationUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'location/sublocation_update.html'
    form_class = SubLocationForm
    success_url = reverse_lazy('sublocation')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(SubLocation, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)

class SubLocationDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'location/sublocation_delete.html'
    success_url = reverse_lazy('sublocation')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(SubLocation, pk=pk_)

#Field Views
@login_required()
def field_view(request):
    tenant = get_tenant(request)
    fields = Field.objects.filter(tenant=tenant)

    return render(request, 'location/field.html',{'fields':fields, 'tenant':tenant})

@login_required()
def field_create_view(request):
    form = FieldForm()
    if request.method == 'POST':
        form = FieldForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/location/field/')
        else:
            form = FieldForm()
    return render(request, 'location/field_create.html', {'form' : form})

#class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class FieldUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'location/field_update.html'
    form_class = FieldForm
    success_url = reverse_lazy('field')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Field, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)

class FieldDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'location/field_delete.html'
    success_url = reverse_lazy('field')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Field, pk=pk_)