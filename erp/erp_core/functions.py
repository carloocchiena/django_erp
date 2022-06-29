from . import models

def sum_active_invoices():
    """Sum all the invoices that the company issued to all its ctps"""
    active_invoices = []
    query = models.Invoice.objects.all().filter(kind='ACTIVE')
    
    for company in query:
        active_invoices.append(company)
    
    return active_invoices
        
if __name__ == '__main__':
    sum_active_invoices()
