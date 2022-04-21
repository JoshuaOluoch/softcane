from .models import (StockCategory, StockItem, FuelType, Tank, FuelPump, FuelReadings,
                      StockArticleIssue, StockArticleAdjustment)
from .forms import (StockCategoryForm, StockItemForm, FuelTypeForm, TankForm, FuelPumpForm, FuelReadingsForm,
                     StockArticleIssueForm, StockArticleAdjustmentForm)

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


# StockCategory Views
@login_required()
def stock_category_view(request):
    tenant = get_tenant(request)
    stock_categories = StockCategory.objects.filter(tenant=tenant)

    return render(request, 'stock/stock_category.html', {'stock_categories': stock_categories, 'tenant': tenant})


@login_required()
def stock_category_create_view(request):
    form = StockCategoryForm()
    if request.method == 'POST':
        form = StockCategoryForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/stock/')
        else:
            form = StockCategoryForm()
    return render(request, 'stock/stock_category_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class StockCategoryUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'stock/stock_category_update.html'
    form_class = StockCategoryForm
    success_url = reverse_lazy('stock_categories')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(StockCategory, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class StockCategoryDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'stock/stock_category_delete.html'
    success_url = reverse_lazy('stock_categories')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(StockCategory, pk=pk_)


# Stock Items View
@login_required()
def stock_item_view(request):
    tenant = get_tenant(request)
    stock_items = StockItem.objects.filter(tenant=tenant)

    return render(request, 'stock/stock_item.html', {'stock_items': stock_items, 'tenant': tenant})


@login_required()
def stock_item_create_view(request):
    form = StockItemForm()
    if request.method == 'POST':
        form = StockItemForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/stock/stock_items/')
        else:
            form = StockItemForm()
    return render(request, 'stock/stock_item_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class StockItemUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'stock/stock_item_update.html'
    form_class = StockItemForm
    success_url = reverse_lazy('stock_items')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(StockItem, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class StockItemDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'stock/stock_item_delete.html'
    success_url = reverse_lazy('stock_items')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(StockItem, pk=pk_)


# Fuel Type View
@login_required()
def fuel_type_view(request):
    tenant = get_tenant(request)
    fuel_types = FuelType.objects.filter(tenant=tenant)

    return render(request, 'stock/fuel_type.html', {'fuel_types': fuel_types, 'tenant': tenant})


@login_required()
def fuel_type_create_view(request):
    form = FuelTypeForm()
    if request.method == 'POST':
        form = FuelTypeForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/stock/fuel_type/')
        else:
            form = FuelTypeForm()
    return render(request, 'stock/fuel_type_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class FuelTypeUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'stock/fuel_type_update.html'
    form_class = FuelTypeForm
    success_url = reverse_lazy('fuel_type')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(FuelType, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class FuelTypeDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'stock/fuel_type_delete.html'
    success_url = reverse_lazy('fuel_type')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(FuelType, pk=pk_)


# Tanks View
@login_required()
def tank_view(request):
    tenant = get_tenant(request)
    tanks = Tank.objects.filter(tenant=tenant)

    return render(request, 'stock/tank.html', {'tanks': tanks, 'tenant': tenant})


@login_required()
def tank_create_view(request):
    form = TankForm()
    if request.method == 'POST':
        form = TankForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/stock/tank/')
        else:
            form = TankForm()
    return render(request, 'stock/tank_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class TankUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'stock/tank_update.html'
    form_class = TankForm
    success_url = reverse_lazy('tank')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Tank, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class TankDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'stock/tank_delete.html'
    success_url = reverse_lazy('tank')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Tank, pk=pk_)


# FuelPump View
@login_required()
def fuel_pump_view(request):
    tenant = get_tenant(request)
    fuel_pumps = FuelPump.objects.filter(tenant=tenant)

    return render(request, 'stock/fuel_pump.html', {'fuel_pumps': fuel_pumps, 'tenant': tenant})


@login_required()
def fuel_pump_create_view(request):
    form = FuelPumpForm()
    if request.method == 'POST':
        form = FuelPumpForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/stock/fuel_pump/')
        else:
            form = FuelPumpForm()
    return render(request, 'stock/fuel_pump_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class FuelPumpUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'stock/fuel_pump_update.html'
    form_class = FuelPumpForm
    success_url = reverse_lazy('fuel_pump')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(FuelPump, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class FuelPumpDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'stock/fuel_pump_delete.html'
    success_url = reverse_lazy('fuel_pump')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(FuelPump, pk=pk_)




# Stock Article Issue
@login_required()
def stock_article_issue_view(request):
    tenant = get_tenant(request)
    stock_article_issue = StockArticleIssue.objects.filter(tenant=tenant)

    return render(request, 'stock/stock_article_issue.html',
                  {'stock_article_issue': stock_article_issue, 'tenant': tenant})


@login_required()
def stock_article_issue_create_view(request):
    form = StockArticleIssueForm()
    if request.method == 'POST':
        form = StockArticleIssueForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/stock/stock_article_issue/')
        else:
            form = StockArticleIssueForm()
    return render(request, 'stock/stock_article_issue_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class StockArticleIssueUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'stock/stock_article_issue_update.html'
    form_class = StockArticleIssueForm
    success_url = reverse_lazy('stock_article_issue')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(StockArticleIssue, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class StockArticleIssueDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'stock/stock_article_issue_delete.html'
    success_url = reverse_lazy('stock_article_issue')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(StockArticleIssue, pk=pk_)


# Stock Article Adjustment
@login_required()
def stock_article_adjustment_view(request):
    tenant = get_tenant(request)
    stock_article_adjustment = StockArticleAdjustment.objects.filter(tenant=tenant)

    return render(request, 'stock/stock_article_adjustment.html',
                  {'stock_article_adjustment': stock_article_adjustment, 'tenant': tenant})


@login_required()
def stock_article_adjustment_create_view(request):
    form = StockArticleAdjustmentForm()
    if request.method == 'POST':
        form = StockArticleAdjustmentForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/stock/stock_article_adjustment/')
        else:
            form = StockArticleAdjustmentForm()
    return render(request, 'stock/stock_article_adjustment_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class StockArticleAdjustmentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'stock/stock_article_adjustment_update.html'
    form_class = StockArticleAdjustmentForm
    success_url = reverse_lazy('stock_article_adjustment')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(StockArticleAdjustment, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class StockArticleAdjustmentDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'stock/stock_article_adjustment_delete.html'
    success_url = reverse_lazy('stock_article_adjustment')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(StockArticleAdjustment, pk=pk_)


#######################################################################################
##### Fuel Readings Views ###############################################################
# FuelPump View
@login_required()
def fuel_readings_view(request):
    tenant = get_tenant(request)
    fuel_readings = FuelReadings.objects.filter(tenant=tenant)

    return render(request, 'stock/fuel_readings.html', {'fuel_readings': fuel_readings, 'tenant': tenant})


@login_required()
def fuel_readings_create_view(request):
    form = FuelReadingsForm()
    if request.method == 'POST':
        form = FuelReadingsForm(request.POST)
        if form.is_valid():
            form.instance.tenant = get_tenant(request)
            form.save(commit=True)
            return redirect('/stock/fuel_readings/')
        else:
            form = FuelReadingsForm()
    return render(request, 'stock/fuel_readings_create.html', {'form': form})


# class DesignerEntryUpdateView(LoginRequiredMixin,UpdateView):
class FuelReadingsUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'stock/fuel_readings_update.html'
    form_class = FuelReadingsForm
    success_url = reverse_lazy('fuel_readings')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(FuelReadings, pk=pk_)

    def form_valid(self, form):
        return super().form_valid(form)


class FuelReadingsDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'stock/fuel_readings_delete.html'
    success_url = reverse_lazy('fuel_readings')

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(FuelReadings, pk=pk_)
