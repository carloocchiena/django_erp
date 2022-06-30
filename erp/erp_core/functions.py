from . import models

def sum_active_invoices():
    """Sum all the invoices that the company issued to all its ctps"""
    kind = 'ACTIVE'
    payment_dictionary = {}
    invoice_query = models.Invoice.objects.all().filter(kind=kind)
    payment_query = models.Payment.objects.all().filter(kind=kind)
    company_query = models.Company.objects.all()
    
    company_pks = invoice_query.values_list('receiver', flat=True)
    
    temp_list = list(company_query.filter(pk__in=company_pks))

    print(f"company_pk:{(list(company_pks))}")
    print(f"company_list:{(list(company_query.filter(pk__in=company_pks)))}")
    print(f"single_company:{(temp_list[0])}")
    print(f"queryset:{(invoice_query.values_list('receiver', flat=True))}")
    
    
    #arrivato qui, tutto da costruire ma siamo a metà strada dai
    
    """
    for company in temp_list:
        value = payment_query.values_list(company)    
        payment_dictionary[company] = value
    
    print(payment_dictionary)
    """
    
    
    return list("PIPPO")
      
        
if __name__ == '__main__':
    sum_active_invoices()
