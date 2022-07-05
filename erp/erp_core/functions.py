from django.db.models import Sum

from . import models

def active_credit_calculator() -> dict:
    """Sum all the invoices that the company issued to all its ctps,
    and retrieve the open credits.
    
    RETURN dictionary
    """
    kind = 'ACTIVE'
    payment_dictionary = {}
    
    company_pks = models.Invoice.objects.all().filter(kind=kind).values_list('receiver', flat=True)
    company_list = list(models.Company.objects.all().filter(pk__in=company_pks))
    
    for company in company_list:
        payment = models.Payment.objects.all().filter(kind=kind, sender__name=company).aggregate(Sum('amount'))['amount__sum'] 
        invoice = models.Invoice.objects.all().filter(kind=kind, receiver__name=company).aggregate(Sum('amount'))['amount__sum']
        
        if payment is None:
            payment = 0
        elif invoice is None:
            invoice = 0
        
        payment_dictionary[company] = {'Bills':invoice, 'Payment':payment, 'Outstanding':invoice - payment}

    print(payment_dictionary)
    
    return payment_dictionary
      
if __name__ == '__main__':
    active_credit_calculator()


    """
    print(f"company_pk:{(list(company_pks))}")
    print(f"company_list:{(list(company_query.filter(pk__in=company_pks)))}")
    print(f"single_company:{(temp_list[0])}")
    print(f"queryset:{(invoice_query.values_list('receiver', flat=True))}")
    print(f"paymnent_query: {models.Payment.objects.all().filter(kind=kind, sender__name='BETA').values('amount')}")
    sum = models.Payment.objects.all().filter(kind=kind, sender__name='BETA').aggregate(Sum('amount'))['amount__sum']
    """