import csv # per csv export, tbc
from django.db.models import Sum
from django.http import HttpResponse # per csv export, tbc
from django.utils.text import slugify # per csv export, tbc

from . import models

def kind_list_updater() -> list:
    """Create the list of valid kind type from models.py"""
    valid_kind = []
    
    for kind in models.Payment.Kind.choices():
        valid_kind.append(kind[0])

    return valid_kind    

def kind_checker(kind:str) -> str:
    """Check formal correctness of input values"""
    
    valid_kind = kind_list_updater()
    
    if kind not in valid_kind:
        kind = 'ACTIVE'
    
    if kind == 'ACTIVE':
        initiator = 'receiver'
    else: 
        initiator = 'sender'
        
    return kind, initiator

def credit_calculator(kind:str='ACTIVE') -> dict:
    """Sum all the invoices that the company issued to all its ctps,
    and retrieve the open credits.
    
    kind = accordingly to models.Invoice, should be 'ACTIVE' or 'PASSIVE'
    
    RETURN dictionary
    
    These snippets are used to print the value from the query if a check is needed
    also to be used straight in the shell
    # print(f"company_pk:{(list(company_pks))}")
    # print(f"company_list:{(list(company_query.filter(pk__in=company_pks)))}")
    # print(f"single_company:{(temp_list[0])}")
    # print(f"queryset:{(invoice_query.values_list('receiver', flat=True))}")
    # print(f"paymnent_query: {models.Payment.objects.all().filter(kind=kind, sender__name='BETA').values('amount')}")
    
    """
    payment_dictionary = {}
    kind, initiator = kind_checker(kind)
    
    company_pks = models.Invoice.objects.all().filter(kind=kind).values_list(initiator, flat=True)
    company_list = list(models.Company.objects.all().filter(pk__in=company_pks))
    
    for company in company_list:
        if kind == 'ACTIVE':
            payment = models.Payment.objects.all().filter(kind=kind, sender__name=company).aggregate(Sum('amount'))['amount__sum'] 
            invoice = models.Invoice.objects.all().filter(kind=kind, receiver__name=company).aggregate(Sum('amount'))['amount__sum']
        elif kind == 'PASSIVE':
            payment = models.Payment.objects.all().filter(kind=kind, receiver__name=company).aggregate(Sum('amount'))['amount__sum'] 
            invoice = models.Invoice.objects.all().filter(kind=kind, sender__name=company).aggregate(Sum('amount'))['amount__sum']
    
        if payment is None:
            payment = 0
        
        if invoice is None:
            invoice = 0
        
        payment_dictionary[company] = {'Bills':invoice, 'Payment':payment, 'Outstanding':invoice - payment}
    
    return payment_dictionary
      
#### WIP CSV TBDELETED      
# wip non so bene come chiamarla solo da funzione 
def generate_csv(request, context) -> csv:
    """Generate a csv file of the context object"""
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition':'attachment; filename="csv_detail.csv"'},
    )
    
    writer = csv.writer(response)
    
    for object in context:
        writer.writerow([context])
    
    return response

# esperimento con una classe
class CSVResponseMixin(object):
    """
    A generic mixin that constructs a CSV response from the context data if
    the CSV export option was provided in the request.
    """
    def render_to_response(self, context, **response_kwargs):
        """
        Creates a CSV response if requested, otherwise returns the default
        template response.
        """
        # Sniff if we need to return a CSV export
        if 'csv' in self.request.GET.get('export', ''):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="%s.csv"' % slugify(context['title'])

            writer = csv.writer(response)
            # Write the data from the context somehow
            for item in context['items']:
                writer.writerow(item)

            return response
        # Business as usual otherwise
        else:
            return super(CSVResponseMixin, self).render(context, **response_kwargs)
    
#### END WIP CSV

if __name__ == '__main__':
    credit_calculator()
