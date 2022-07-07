from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from . import models, forms, filters, functions

class Home(View):
    def get(self, request):
        return render(request, 'erp_core/home.html')
    
class Help(View):
    """Help page"""
    template_name = 'erp_core/help.html'
    
    def get(self, request):
        return render(request, self.template_name)
        
# company management 

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

# invoice management
    
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
    
# payment management

class PaymentCreate(CreateView):
    """Create a new payment"""
    model = models.Payment
    form_class = forms.PaymentForm
    success_url = reverse_lazy('erp_core:payment_list') 
    
class PaymentList(ListView):
    """View all Payments"""
    model = models.Payment
    
    # filter via query
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = filters.PaymentFilter(self.request.GET, queryset=self.get_queryset())
        return context  
    
class PaymentUpdate(UpdateView):
    """Update an Payment"""
    model = models.Payment
    form_class = forms.PaymentForm
    success_url = reverse_lazy('erp_core:payment_list')
    
# pre-made filterd views

class FilteredView(View):
    def get(self, request):
        return render(request, 'erp_core/filtered_view.html')

class InvoiceActive(View):
    """Pre-made filter for active invoices"""
    model = models.Invoice
    template_name = 'erp_core/invoice_active.html'
    
    def get(self, request):
        context = self.model.objects.all().filter(kind='ACTIVE')
        return render(request, self.template_name, {'context': context})

class InvoicePassive(View):
    """Pre-made filter for passive invoices"""
    model = models.Invoice
    template_name = 'erp_core/invoice_passive.html'
    
    def get(self, request):
        context = self.model.objects.all().filter(kind='PASSIVE')
        return render(request, self.template_name, {'context': context}) 
    
class PaymentActive(View):
    """Pre-made filter for active payments"""
    model = models.Payment
    template_name = 'erp_core/payment_active.html'
    
    def get(self, request):
        context = self.model.objects.all().filter(kind='ACTIVE')
        return render(request, self.template_name, {'context': context})

class PaymentPassive(View):
    """Pre-made filter for passive payments"""
    model = models.Payment
    template_name = 'erp_core/payment_passive.html'
    
    def get(self, request):
        context = self.model.objects.all().filter(kind='PASSIVE')
        return render(request, self.template_name, {'context': context}) 
    
# credit management

class ActiveCheck(View):
    """View to show the credit balance"""
    template_name = 'erp_core/active_check.html'
    
    def get(self, request):
        context = functions.credit_calculator('ACTIVE')
        return render(request, self.template_name, {'context': context})
    
class PassiveCheck(View):
    """View to show the credit balance"""
    template_name = 'erp_core/active_check.html'
    
    def get(self, request):
        context = functions.credit_calculator('PASSIVE')
        return render(request, self.template_name, {'context': context})
    