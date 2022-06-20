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