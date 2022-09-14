import csv

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import permissions, viewsets

from . import models, forms, filters, functions, serializers


# GENERAL WEBSITE NAVIGATION

class Home(View):
    def get(self, request):
        return render(request, 'erp_core/home.html')
    
    
class Help(View):
    """Help page"""
    template_name = 'erp_core/help.html'
    
    def get(self, request):
        return render(request, self.template_name)
    

class Feature(View):
    """Feature page"""
    template_name = 'erp_core/feature.html'
    
    def get(self, request):
        return render(request, self.template_name)
        
        
# COMPANY MANAGEMENT 

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
    
    
# WIP
    
class CompanyClone(UpdateView):
    """Clone a company"""
    model = models.Company
    form_class = forms.CompanyForm
    success_url = reverse_lazy('erp_core:company_list')
    
    
# PRODUCT MANAGEMENT

class ProductCreate(CreateView):
    """Create a new product"""
    model = models.Product
    form_class = forms.ProductForm
    success_url = reverse_lazy('erp_core:product_list') 
    
    
class ProductDetail(DetailView):
    """View a single product"""
    model = models.Product
    slug_field = 'id'
    
    
class ProductList(ListView):
    """View all profiles"""
    model = models.Product
    
    # filter via query
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = filters.ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context
    
    
class ProductUpdate(UpdateView):
    """Update a product"""
    model = models.Product
    form_class = forms.ProductForm
    success_url = reverse_lazy('erp_core:product_list')


# INVOICE MANAGEMENT
    
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
    
    
# PAYMENT MANAGEMENT

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
    
    
# PRE-MADE FILTERS

class FilteredView(View):
    """Main page for all the filters"""
    def get(self, request):
        return render(request, 'erp_core/filtered_view.html')


class InvoiceActive(View):
    """Pre-made filter for active invoices"""
    model = models.Invoice
    template_name = 'erp_core/invoice_active.html'
    
    def get(self, request):
        context = self.model.objects.all().filter(kind='ACTIVE')
        return render(request, self.template_name, {'context': context})
    
    
class InvoiceActiveOverdue(View):
    """Pre-made filter for overdue active invoices"""
    model = models.Invoice
    template_name = 'erp_core/invoice_active_overdue.html'
    
    def get(self, request):
        context = self.model.objects.all().filter(kind='ACTIVE', status='UNPAID')
        return render(request, self.template_name, {'context': context})


class InvoicePassive(View):
    """Pre-made filter for passive invoices"""
    model = models.Invoice
    template_name = 'erp_core/invoice_passive.html'
    
    def get(self, request):
        context = self.model.objects.all().filter(kind='PASSIVE')
        return render(request, self.template_name, {'context': context}) 
    
    
class InvoicePassiveOverdue(View):
    """Pre-made filter for overdue active invoices"""
    model = models.Invoice
    template_name = 'erp_core/invoice_passive_overdue.html'
    
    def get(self, request):
        context = self.model.objects.all().filter(kind='PASSIVE', status='UNPAID')
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


# CREDIT MANAGEMENT

class CheckActive(View):
    """View to show the credit balance"""
    template_name = 'erp_core/check_active.html'
    
    def get(self, request):
        context = functions.credit_calculator('ACTIVE')
        return render(request, self.template_name, {'context': context})
    
    
class CheckPassive(View):
    """View to show the credit balance"""
    template_name = 'erp_core/check_passive.html'
    
    def get(self, request):
        context = functions.credit_calculator('PASSIVE')
        return render(request, self.template_name, {'context': context})


# CSV EXPORT

class CsvExport(View):
    """Generate a csv file of the context object"""
    template_name = 'erp_core/csv_export.html'
    
    def get(self, request) -> csv:
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition':'attachment; filename="csv_detail.csv"'},
        )
        
        # this allows to scale on many other CSV export just managing the url param
        if 'invoice' in self.request.GET:
            model = models.Invoice.objects.all().values()
        elif 'company' in self.request.GET:
            model = models.Company.objects.all().values()
        elif 'product' in self.request.GET:
            model = models.Product.objects.all().values()
        else:
            raise Http404
        
        writer = csv.writer(response)
        
        for item in model:
            writer.writerow([item])
            
        return response
    
    
# API MANAGEMENT

class CompanyViewSet(viewsets.ModelViewSet):
    """Return our API object.
    Endpoint: "http://127.0.0.1:8000/api/v1/company/"
    """
    queryset = models.Company.objects.all().order_by('name')
    serializer_class = serializers.CompanySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class ProductViewSet(viewsets.ModelViewSet):
    """Return our API object
    Endpoint: "http://127.0.0.1:8000/api/v1/product/"
    """
    queryset = models.Product.objects.all().order_by('name')
    serializer_class = serializers.ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class InvoiceViewSet(viewsets.ModelViewSet):
    """Return our API object
    Endpoint: "http://127.0.0.1:8000/api/v1/invoice/"
    """
    queryset = models.Invoice.objects.all()
    serializer_class = serializers.InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class PaymentViewSet(viewsets.ModelViewSet):
    """Return our API object
    Endpoint: "http://127.0.0.1:8000/api/v1/payment/"
    """
    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    