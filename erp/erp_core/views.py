import csv

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
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
    
# product management

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

# invoice management
    
class InvoiceCreate(CreateView):
    """Create a new invoice"""
    model = models.Invoice
    form_class = forms.InvoiceForm
    success_url = reverse_lazy('erp_core:invoice_list') 
    
    #wip per modificare quantità prodotto
    def post(self, request):
        """Manage invoice creation and update of the products quantities"""
        form = forms.InvoiceForm(request.POST)
        product_name = models.Product.objects.get(pk=form['product'].value()).name
        product_quantity = models.Product.objects.get(name=product_name).quantity
        print(product_quantity)
        update_quantity = int(form['product_quantity'].value())
        kind = form['kind'].value()
        print(update_quantity)
        
        if form.is_valid():
            if kind == 'ACTIVE':
                product_quantity -= update_quantity
            else:
                product_quantity += update_quantity
            product_quantity.save()
            product_name.save()  # arrivato qui, tutto ok ma non salva; provare con https://stackoverflow.com/questions/68506395/how-can-i-update-the-field-of-a-model-from-another-model-field-in-django 
            models.Product.objects.all().save()
            form.save()
            return redirect('erp_core:invoice_list')
        else:
            return render(request, self.template_name)
                
            
    
    
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

# credit management

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

# export to CSV

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
            model = models.Invoice.objects.all()
        elif 'company' in self.request.GET:
            model = models.Company.objects.all()
        elif 'product' in self.request.GET:
            model = models.Product.objects.all()
        else:
            raise Http404
        
        writer = csv.writer(response)
        
        for item in model:
            writer.writerow([item])
            print(item)
            
        return response
    