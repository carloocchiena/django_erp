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
        
class InvoiceFilter(django_filters.FilterSet):
    """Allow search over the invoice DB"""
    class Meta:
        model = models.Invoice
        fields = {
            #'sender': ['icontains', 'Company__name'],  # how to use icontains with foreign key https://django-filter.readthedocs.io/en/stable/guide/usage.html?#generating-filters-with-meta-fields
            #'receiver': ['icontains'],
            'date': ['icontains'], 
            'number': ['icontains'], 
            'amount': ['icontains'], 
            'kind': ['icontains'], 
            'due_date': ['icontains'], 
            'status': ['icontains'], 
            'notes': ['icontains'], 
        }
        