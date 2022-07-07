from django.db.models import Sum

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
      
if __name__ == '__main__':
    credit_calculator()


    """
    # these snippets are used to print the value from the query if a check is needed
    # even used straigth in the shell
    print(f"company_pk:{(list(company_pks))}")
    print(f"company_list:{(list(company_query.filter(pk__in=company_pks)))}")
    print(f"single_company:{(temp_list[0])}")
    print(f"queryset:{(invoice_query.values_list('receiver', flat=True))}")
    print(f"paymnent_query: {models.Payment.objects.all().filter(kind=kind, sender__name='BETA').values('amount')}")
    sum = models.Payment.objects.all().filter(kind=kind, sender__name='BETA').aggregate(Sum('amount'))['amount__sum']
    """
    