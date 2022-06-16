from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from . import models, forms

class Home(View):
    def get(self, request):
        return render(request, 'erp_core/home.html')
    
class CompanyCreate(CreateView):
    """Create a new company"""
    model = models.Company
    form_class = forms.CompanyForm
    success_url = reverse_lazy('erp_core:home') # aggiornare con company list
    
class InvoiceCreate(CreateView):
    """Create a new invoice"""
    model = models.Invoice
    form_class = forms.InvoiceForm
    success_url = reverse_lazy('erp_core:home') # aggiornare con invoice list

class CompanyList(ListView):
    """View all profiles"""
    model = models.Company
    
class InvoiceList(ListView):
    """View all invoices"""
    model = models.Invoice  
    
class CompanyDetail(DetailView):
    """View a single profile"""
    model = models.Company
    slug_field = 'vat_id'
    