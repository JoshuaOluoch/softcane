from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
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

class IndexView(LoginRequiredMixin, TemplateView):
	login_url = 'users/login/'
	redirect_field_name = 'redirect_to'
	template_name = "dashboard/index.html"
	#now = datetime.now()

	#def get_context_data(self, **kwargs):
	#	context = super().get_context_data(**kwargs)
	#	now = datetime.now()
        #context['tenant'] = get_tenant()
		#context['article_this_year'] = Article.objects.filter(rated=True).filter(submission_date__gte=str(now.year)+"-01-01").count()
		#context['article_this_month'] = Article.objects.filter(rated=True).filter(submission_date__gte=str(now.year)+"-0"+str(now.month)+"-01").count()
		#context['article_this_week'] = Article.objects.filter(rated=True).filter(submission_date__gte=datetime.today()-timedelta(days= datetime.today().weekday()+2)).count()
		#context['article_count'] =Article.objects.filter(rated=True).count()

