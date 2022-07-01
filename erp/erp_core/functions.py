from django.db.models import Sum

from . import models

def sum_active_invoices():
    """Sum all the invoices that the company issued to all its ctps"""
    kind = 'ACTIVE'
    payment_dictionary = {}
    
    # qui tutto da ottimizzare\potare
    
    invoice_query = models.Invoice.objects.all().filter(kind=kind)
    payment_query = models.Payment.objects.all().filter(kind=kind)
    company_query = models.Company.objects.all()
    
    company_pks = invoice_query.values_list('receiver', flat=True)
    
    temp_list = list(company_query.filter(pk__in=company_pks))

    print(f"company_pk:{(list(company_pks))}")
    print(f"company_list:{(list(company_query.filter(pk__in=company_pks)))}")
    print(f"single_company:{(temp_list[0])}")
    print(f"queryset:{(invoice_query.values_list('receiver', flat=True))}")
    print(f"paymnent_query: {models.Payment.objects.all().filter(kind=kind, sender__name='BETA').values('amount')}")
    
    sum = models.Payment.objects.all().filter(kind=kind, sender__name='BETA').aggregate(Sum('amount'))['amount__sum']
    print(sum) # print 1000
    
    for company in temp_list:
       value = models.Payment.objects.all().filter(kind=kind, sender__name=company).aggregate(Sum('amount'))['amount__sum']    
       payment_dictionary[company] = value
       print(company)
    
    print(value) 
    print(payment_dictionary)
    # ok ora ho la somma dei pagamenti, devo incrociare con la parte di fatture, phew!
    
    return payment_dictionary
      
        
if __name__ == '__main__':
    sum_active_invoices()


# references:
# https://stackoverflow.com/questions/8616343/django-calculate-the-sum-of-the-column-values-through-query 