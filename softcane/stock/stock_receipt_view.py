from django.db import transaction
from .models import StockArticleReceipt, StockArticleReceiptItem
from .stock_receipt_form import  StockArticleReceiptItemFormSet

#from location.models import Branch
from tenant.models import Tenant

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
#from datetime import datetime, timedelta
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



class StockArticleReceiptList(ListView):
    model = StockArticleReceipt
    paginate_by = 50
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'stock/stock_article_receipt.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stock_article_receipt'] = StockArticleReceipt.objects.filter(tenant=get_tenant(self.request))
        return context


class StockArticleReceiptCreate(LoginRequiredMixin,CreateView):
    model = StockArticleReceipt
    fields = ['internal_no', 'reference_no', 'date', 'supplier',  'remark']


class StockArticleReceiptItemCreate(LoginRequiredMixin,CreateView):
    model = StockArticleReceipt
    fields =['internal_no', 'reference_no', 'date', 'supplier',  'remark']
    success_url = reverse_lazy('stock_article_receipt')

    def get_context_data(self, **kwargs):
        data = super(StockArticleReceiptItemCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['stock_article_receipt_item'] = StockArticleReceiptItemFormSet(self.request.POST)
        else:
            data['stock_article_receipt_item'] = StockArticleReceiptItemFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        stock_article_receipt_item = context['stock_article_receipt_item']
        with transaction.atomic():
            self.object = form.save(commit=False)
            self.object.tenant =get_tenant(self.request)
            self.object.posted_by = self.request.user
            self.object.save()

            if stock_article_receipt_item.is_valid():
                items = stock_article_receipt_item.save(commit=False)
                for item in items:
                    item.receipt_header_id = self.object
                    item.save()
                #stock_article_receipt_item.instance = self.object
                #stock_article_receipt_item.save()
        return super(StockArticleReceiptItemCreate, self).form_valid(form)


class StockArticleReceiptUpdate(LoginRequiredMixin, UpdateView):
    model = StockArticleReceipt
    fields = ['internal_no', 'reference_no', 'date', 'supplier',  'remark']
    success_url = reverse_lazy('stock_article_receipt')


class StockArticleReceiptItemUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    model = StockArticleReceipt
    fields = ['internal_no', 'reference_no', 'date', 'supplier',  'remark']
    success_url = reverse_lazy('stock_article_receipt')

    def get_context_data(self, **kwargs):
        data = super(StockArticleReceiptItemUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['stock_article_receipt_item'] = StockArticleReceiptItemFormSet(self.request.POST)
        else:
            data['stock_article_receipt_item'] = StockArticleReceiptItemFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        stock_article_receipt_item = context['stock_article_receipt_item']
        with transaction.atomic():
            self.object = form.save()

            if stock_article_receipt_item.is_valid():
                items = stock_article_receipt_item.save(commit=False)
                for item in items:
                    item.receipt_header_id = self.object
                    item.save()
        return super(StockArticleReceiptItemUpdate, self).form_valid(form)


class StockArticleReceiptDelete(LoginRequiredMixin,DeleteView):
    login_url = 'users/login/'
    redirect_field_name = 'redirect_to'
    model = StockArticleReceipt
    success_url = reverse_lazy('stock_article_receipt')
