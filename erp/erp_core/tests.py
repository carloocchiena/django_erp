from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import TestCase, Client

from rest_framework.test import APITestCase, force_authenticate

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
        
    def test_company_name_label(self):
        obj = models.Company.objects.get(id=1)
        field_label = obj._meta.get_field('name').verbose_name
        
        self.assertEqual(field_label, 'name')
        
    def test_company_name_length(self):
        obj = models.Company.objects.get(id=1)
        max_length = obj._meta.get_field('name').max_length
        
        self.assertEqual(max_length, 100)
    
    def test_company_vat_label(self):
        obj = models.Company.objects.get(id=1)
        field_label = obj._meta.get_field('vat_id').verbose_name
        
        self.assertEqual(field_label, 'vat id')
        
    def test_company_vat_length(self):
        obj = models.Company.objects.get(id=1)
        max_length = obj._meta.get_field('vat_id').max_length
        
        self.assertEqual(max_length, 15)
        
    def test_company_industry_label(self):
        obj = models.Company.objects.get(id=1)
        field_label = obj._meta.get_field('industry').verbose_name
        
        self.assertEqual(field_label, 'industry')
        
    def test_company_industry_length(self):
        obj = models.Company.objects.get(id=1)
        max_length = obj._meta.get_field('industry').max_length
        
        self.assertEqual(max_length, 15)
        
    def test_company_city_label(self):
        obj = models.Company.objects.get(id=1)
        field_label = obj._meta.get_field('city').verbose_name
        
        self.assertEqual(field_label, 'city')
        
    def test_company_city_length(self):
        obj = models.Company.objects.get(id=1)
        max_length = obj._meta.get_field('city').max_length
        
        self.assertEqual(max_length, 20)
        
    def test_company_address_label(self):
        obj = models.Company.objects.get(id=1)
        field_label = obj._meta.get_field('address').verbose_name
        
        self.assertEqual(field_label, 'address')
        
    def test_company_address_length(self):
        obj = models.Company.objects.get(id=1)
        max_length = obj._meta.get_field('address').max_length
        
        self.assertEqual(max_length, 100)
        
    def test_company_zip_code_label(self):
        obj = models.Company.objects.get(id=1)
        field_label = obj._meta.get_field('zip_code').verbose_name
        
        self.assertEqual(field_label, 'zip code')
        
    def test_company_zip_code_length(self):
        obj = models.Company.objects.get(id=1)
        max_length = obj._meta.get_field('zip_code').max_length
        
        self.assertEqual(max_length, 10)
        
    def test_company_country_label(self):
        obj = models.Company.objects.get(id=1)
        field_label = obj._meta.get_field('country').verbose_name
        
        self.assertEqual(field_label, 'country')
        
    def test_company_country_length(self):
        obj = models.Company.objects.get(id=1)
        max_length = obj._meta.get_field('country').max_length
        
        self.assertEqual(max_length, 10)
        
    def test_company_website_label(self):
        obj = models.Company.objects.get(id=1)
        field_label = obj._meta.get_field('website').verbose_name
        
        self.assertEqual(field_label, 'website')
        
        
    def test_company_notes_label(self):
        obj = models.Company.objects.get(id=1)
        field_label = obj._meta.get_field('notes').verbose_name
        
        self.assertEqual(field_label, 'notes')
        
    def test_object_name(self):
        obj = models.Company.objects.get(id=1)
        expected_object_name = f'{obj.name.upper()}'
        
        self.assertEqual(str(obj), expected_object_name)        
        
    
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
        
    def test_product_name_label(self):
        obj = models.Product.objects.get(id=1)
        field_label = obj._meta.get_field('name').verbose_name
        
        self.assertEqual(field_label, 'name')
        
    def test_product_name_length(self):
        obj = models.Product.objects.get(id=1)
        max_length = obj._meta.get_field('name').max_length
        
        self.assertEqual(max_length, 30)
        
        
    def test_product_description_label(self):
        obj = models.Product.objects.get(id=1)
        field_label = obj._meta.get_field('description').verbose_name
        
        self.assertEqual(field_label, 'description')
        
    def test_product_description_length(self):
        obj = models.Product.objects.get(id=1)
        max_length = obj._meta.get_field('description').max_length
        
        self.assertEqual(max_length, 500)
        
        
    def test_product_quantity_label(self):
        obj = models.Product.objects.get(id=1)
        field_label = obj._meta.get_field('quantity').verbose_name
        
        self.assertEqual(field_label, 'quantity')
        
        
    def test_product_price_label(self):
        obj = models.Product.objects.get(id=1)
        field_label = obj._meta.get_field('price').verbose_name
        
        self.assertEqual(field_label, 'price')
        
        
    def test_product_refill_label(self):
        obj = models.Product.objects.get(id=1)
        field_label = obj._meta.get_field('refill').verbose_name
        
        self.assertEqual(field_label, 'refill')
        
        
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
        
    
class PaymentTestCase(TestCase):
    """Test the generation of a new payment"""
    def setUp(self):
        models.Company.objects.create(name='ALFA', vat_id='123456', industry='TECH', city='GENOVA', address='VIA ROMA 1', zip_code='16100', country='ITALY', website='', notes='')
        
        models.Company.objects.create(name='MY COMPANY', vat_id='012345', industry='TECH', city='GENOVA', address='VIA ROMA 1', zip_code='16100', country='ITALY', website='', notes='')
        
        models.Payment.objects.create(sender=models.Company.objects.get(name='ALFA'), receiver=models.Company.objects.get(name='MY COMPANY'), kind='ACTIVE', date='2022-01-01', amount=1000, notes='TBA')
        
    def test_payment_set_up(self):
        alfa_payment = models.Payment.objects.get(sender=1)

        self.assertEqual(alfa_payment.amount, 1000)


# API test cases

class ApiTestCase(APITestCase):
    """Test connection to APIs"""
    def setUp(self):
        self.username = 'john_doe'
        self.password = 'foobar'
        self.user = User.objects.create(username=self.username, password=self.password)
        self.client.force_authenticate(user=self.user)
        
        
    def test_company_api_get(self):
        response = self.client.get('/api/v1/company/')
        self.assertEqual(response.status_code, 200)
        
    def test_product_api_get(self):
        response = self.client.get('/api/v1/product/')
        self.assertEqual(response.status_code, 200)
        
    def test_invoice_api_get(self):
        response = self.client.get('/api/v1/invoice/')
        self.assertEqual(response.status_code, 200)
        
    def test_payment_api_get(self):
        response = self.client.get('/api/v1/payment/')
        self.assertEqual(response.status_code, 200)
        
                
                
                
