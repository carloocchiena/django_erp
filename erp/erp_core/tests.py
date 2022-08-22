from django.db import IntegrityError

from django.test import TestCase

from . import models, forms


# Model test cases

class CompanyTestCase(TestCase):
    """Test the generation of a new company"""
    def setUp(self):
        models.Company.objects.create(name='ALFA', vat_id='123456', industry='TECH', city='GENOVA', address='VIA ROMA 1', zip_code='16100', country='ITALY', website='', notes='')
        
        models.Company.objects.create(name='BETA', vat_id='1234567', industry='TECH', city='GENOVA', address='VIA ROMA 1', zip_code='16100', country='ITALY', website='', notes='')
        
    def test_company_set_up(self):
        alfa = models.Company.objects.get(name='ALFA')
        beta = models.Company.objects.get(name='BETA')
        
        self.assertEqual(alfa.vat_id, '123456')
        self.assertEqual(beta.industry, 'TECH')
        
    
class DuplicatedCompanyTestCase(TestCase):
    """Test the generation of two companies with same vat_id"""
    def vat_is_duplicated(self, vat_id):
        models.Company.objects.create(name='ALFA', vat_id=vat_id, industry='TECH', city='GENOVA', address='VIA ROMA 1', zip_code='16100', country='ITALY', website='', notes='')
        
        models.Company.objects.create(name='BETA', vat_id=vat_id, industry='TECH', city='GENOVA', address='VIA ROMA 1', zip_code='16100', country='ITALY', website='', notes='')
     
    def test_duplicate_vat(self):    
        with self.assertRaises(IntegrityError):
            self.vat_is_duplicated('123456')
            
            
class ProductTestCase(TestCase):
    """Test the generation of a new product"""
    def setUp(self):
        models.Product.objects.create(name='ALFA', description='A PRODUCT', quantity='50', price='100', refill=True)
        
    def test_product_set_up(self):
        alfa = models.Product.objects.get(name='ALFA')
        
        self.assertEqual(alfa.quantity, 50)
        
        
class InvoiceTestCase(TestCase):
    """Test the generation of a new invoice and the impact over product quantity"""
    def setUp(self):       
        models.Company.objects.create(name='ALFA', vat_id='123456', industry='TECH', city='GENOVA', address='VIA ROMA 1', zip_code='16100', country='ITALY', website='', notes='')
        
        models.Company.objects.create(name='MY COMPANY', vat_id='012345', industry='TECH', city='GENOVA', address='VIA ROMA 1', zip_code='16100', country='ITALY', website='', notes='')
        
        models.Product.objects.create(name='ALFA', description='A PRODUCT', quantity=50, price=100, refill=True)
        
        models.Invoice.objects.create(sender=models.Company.objects.get(name='ALFA'), receiver=models.Company.objects.get(name='MY COMPANY'), date='2022-01-01', number='1', amount=1000, kind='ACTIVE', product=models.Product.objects.get(name='ALFA'), product_quantity=5, due_date='2022-01-01', status='PAID', notes='')
        
    def test_invoice_set_up(self):
        alfa_invoice = models.Invoice.objects.get(sender=1)
        alfa_product = models.Product.objects.get(id=1)

        self.assertEqual(alfa_invoice.kind, 'ACTIVE')
        self.assertEqual(alfa_product.quantity, 55)
                            