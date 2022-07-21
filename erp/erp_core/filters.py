import django_filters

from . import models

class CompanyFilter(django_filters.FilterSet):
    """Allow search over the company DB"""
    class Meta:
        model = models.Company
        fields = {
            'name': ['icontains'],
            'vat_id': ['icontains'],
            'industry': ['icontains'], 
            'city': ['icontains'], 
            'address': ['icontains'], 
            'zip_code': ['icontains'], 
            'country': ['icontains'], 
            'website': ['icontains'], 
            'notes': ['icontains'], 
        }
        
class ProductFilter(django_filters.FilterSet):
    """Allow search over the product DB"""
    class Meta:
        model = models.Product
        fields = {
            'name': ['icontains'], 
            'description': ['icontains'],
            'refill': ['icontains'], 
        }
        
class InvoiceFilter(django_filters.FilterSet):
    """Allow search over the invoice DB"""
    class Meta:
        model = models.Invoice
        fields = {
            'sender__name': ['icontains'], 
            'receiver__name': ['icontains'],
            'date': ['date'], 
            'number': ['icontains'], 
            'amount': ['icontains'], 
            'kind': ['icontains'], 
            'due_date': ['date'], 
            'status': ['icontains'], 
            'notes': ['icontains'], 
        }
        
class PaymentFilter(django_filters.FilterSet):
    """Allow search over the payment DB"""
    class Meta:
        model = models.Payment
        fields = {
            'sender__name': ['icontains'], 
            'receiver__name': ['icontains'],
            'date': ['date'], 
            'amount': ['icontains'], 
            'kind': ['icontains'], 
            'notes': ['icontains'], 
        }
        