from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from . import models, forms, filters

class Home(View):
    def get(self, request):
        return render(request, 'erp_core/home.html')
    
class CompanyCreate(CreateView):
    """Create a new company"""
    model = models.Company
    form_class = forms.CompanyForm
    success_url = reverse_lazy('erp_core:company_list') 
    
class CompanyDetail(DetailView):
    """View a single profile"""
    model = models.Company
    slug_field = 'vat_id'
    
class CompanyList(ListView):
    """View all profiles"""
    model = models.Company
    
    # filter via query
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = filters.CompanyFilter(self.request.GET, queryset=self.get_queryset())
        return context
    
class CompanyUpdate(UpdateView):
    """Update a company"""
    model = models.Company
    form_class = forms.CompanyForm
    success_url = reverse_lazy('erp_core:company_list')
    
class InvoiceCreate(CreateView):
    """Create a new invoice"""
    model = models.Invoice
    form_class = forms.InvoiceForm
    success_url = reverse_lazy('erp_core:invoice_list') 
    
class InvoiceList(ListView):
    """View all invoices"""
    model = models.Invoice
    
    # filter via query
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = filters.InvoiceFilter(self.request.GET, queryset=self.get_queryset())
        return context  
    
class InvoiceUpdate(UpdateView):
    """Update an invoice"""
    model = models.Invoice
    form_class = forms.InvoiceForm
    success_url = reverse_lazy('erp_core:invoice_list')
    

    
    