from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import TestCase, Client
from django.urls import reverse

from rest_framework.test import APITestCase, force_authenticate

from . import models, forms, views


# Model test cases

class CompanyTestCase(TestCase):
    """Test the generation of a new product"""
    def setUp(self):
        models.Company.objects.create(name='ALFA', vat_id='123456', industry='TECH', city='GENOVA', address='VIA ROMA 1', zip_code='16100', country='ITALY', website='', notes='')
        
        models.Company.objects.create(name='BETA', vat_id='1234567', industry='TECH', city='GENOVA', address='VIA ROMA 1', zip_code='16100', country='ITALY', website='', notes='')
        
    def test_product_set_up(self):
        alfa = models.Company.objects.get(name='ALFA')
        beta = models.Company.objects.get(name='BETA')
        
        self.assertEqual(alfa.vat_id, '123456')
        self.assertEqual(beta.industry, 'TECH')
        
    def test_product_name_label(self):
        obj = models.Company.objects.get(id=1)
        field_label = obj._meta.get_field('name').verbose_name
        
        self.assertEqual(field_label, 'name')
        
    def test_product_name_length(self):
        obj = models.Company.objects.get(id=1)
        max_length = obj._meta.get_field('name').max_length
        
        self.assertEqual(max_length, 100)
    
    def test_product_vat_label(self):
        obj = models.Company.objects.get(id=1)
        field_label = obj._meta.get_field('vat_id').verbose_name
        
        self.assertEqual(field_label, 'vat id')
        
    def test_product_vat_length(self):
        obj = models.Company.objects.get(id=1)
        max_length = obj._meta.get_field('vat_id').max_length
        
        self.assertEqual(max_length, 15)
        
    def test_product_industry_label(self):
        obj = models.Company.objects.get(id=1)
        field_label = obj._meta.get_field('industry').verbose_name
        
        self.assertEqual(field_label, 'industry')
        
    def test_product_industry_length(self):
        obj = models.Company.objects.get(id=1)
        max_length = obj._meta.get_field('industry').max_length
        
        self.assertEqual(max_length, 15)
        
    def test_product_city_label(self):
        obj = models.Company.objects.get(id=1)
        field_label = obj._meta.get_field('city').verbose_name
        
        self.assertEqual(field_label, 'city')
        
    def test_product_city_length(self):
        obj = models.Company.objects.get(id=1)
        max_length = obj._meta.get_field('city').max_length
        
        self.assertEqual(max_length, 20)
        
    def test_product_address_label(self):
        obj = models.Company.objects.get(id=1)
        field_label = obj._meta.get_field('address').verbose_name
        
        self.assertEqual(field_label, 'address')
        
    def test_product_address_length(self):
        obj = models.Company.objects.get(id=1)
        max_length = obj._meta.get_field('address').max_length
        
        self.assertEqual(max_length, 100)
        
    def test_product_zip_code_label(self):
        obj = models.Company.objects.get(id=1)
        field_label = obj._meta.get_field('zip_code').verbose_name
        
        self.assertEqual(field_label, 'zip code')
        
    def test_product_zip_code_length(self):
        obj = models.Company.objects.get(id=1)
        max_length = obj._meta.get_field('zip_code').max_length
        
        self.assertEqual(max_length, 10)
        
    def test_product_country_label(self):
        obj = models.Company.objects.get(id=1)
        field_label = obj._meta.get_field('country').verbose_name
        
        self.assertEqual(field_label, 'country')
        
    def test_product_country_length(self):
        obj = models.Company.objects.get(id=1)
        max_length = obj._meta.get_field('country').max_length
        
        self.assertEqual(max_length, 10)
        
    def test_product_website_label(self):
        obj = models.Company.objects.get(id=1)
        field_label = obj._meta.get_field('website').verbose_name
        
        self.assertEqual(field_label, 'website')
                
    def test_product_notes_label(self):
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
        
        models.Invoice.objects.create(sender=models.Company.objects.get(name='ALFA'), receiver=models.Company.objects.get(name='MY COMPANY'), date='2019-03-10 11:16:09.184106+01:00', number='1', amount=1000, kind='ACTIVE', product=models.Product.objects.get(name='ALFA'), product_quantity=5, due_date='2019-03-10 11:16:09.184106+01:00', status='PAID', notes='')
        
    def test_invoice_set_up(self):
        alfa_invoice = models.Invoice.objects.get(sender=1)
        alfa_product = models.Product.objects.get(id=1)

        self.assertEqual(alfa_invoice.kind, 'ACTIVE')
        self.assertEqual(alfa_product.quantity, 55)
            
    def test_invoice_sender_label(self):
        obj = models.Invoice.objects.get(id=1)
        field_label = obj._meta.get_field('sender').verbose_name
        
        self.assertEqual(field_label, 'sender')    
            
    def test_invoice_receiver_label(self):
        obj = models.Invoice.objects.get(id=1)
        field_label = obj._meta.get_field('receiver').verbose_name
        
        self.assertEqual(field_label, 'receiver')   
                
    def test_invoice_date_label(self):
        obj = models.Invoice.objects.get(id=1)
        field_label = obj._meta.get_field('date').verbose_name
        
        self.assertEqual(field_label, 'date')   
                
    def test_invoice_number_label(self):
        obj = models.Invoice.objects.get(id=1)
        field_label = obj._meta.get_field('number').verbose_name
        
        self.assertEqual(field_label, 'number')
                
    def test_invoice_amount_label(self):
        obj = models.Invoice.objects.get(id=1)
        field_label = obj._meta.get_field('amount').verbose_name
        
        self.assertEqual(field_label, 'amount')
                
    def test_invoice_kind_label(self):
        obj = models.Invoice.objects.get(id=1)
        field_label = obj._meta.get_field('kind').verbose_name
        
        self.assertEqual(field_label, 'kind')
                
    def test_invoice_product_label(self):
        obj = models.Invoice.objects.get(id=1)
        field_label = obj._meta.get_field('product').verbose_name
        
        self.assertEqual(field_label, 'product')
                
    def test_invoice_product_quantity_label(self):
        obj = models.Invoice.objects.get(id=1)
        field_label = obj._meta.get_field('product_quantity').verbose_name
        
        self.assertEqual(field_label, 'product quantity')
                
    def test_invoice_due_date_label(self):
        obj = models.Invoice.objects.get(id=1)
        field_label = obj._meta.get_field('due_date').verbose_name
        
        self.assertEqual(field_label, 'due date')
                
    def test_invoice_status_label(self):
        obj = models.Invoice.objects.get(id=1)
        field_label = obj._meta.get_field('status').verbose_name
        
        self.assertEqual(field_label, 'status')
                
    def test_invoice_status_length(self):
        obj = models.Invoice.objects.get(id=1)
        max_length = obj._meta.get_field('status').max_length
        
        self.assertEqual(max_length, 10)
                
    def test_invoice_notes_label(self):
        obj = models.Invoice.objects.get(id=1)
        field_label = obj._meta.get_field('notes').verbose_name
        
        self.assertEqual(field_label, 'notes')
                   
    
    
class PaymentTestCase(TestCase):
    """Test the generation of a new payment"""
    def setUp(self):
        models.Company.objects.create(name='ALFA', vat_id='123456', industry='TECH', city='GENOVA', address='VIA ROMA 1', zip_code='16100', country='ITALY', website='', notes='')
        
        models.Company.objects.create(name='MY COMPANY', vat_id='012345', industry='TECH', city='GENOVA', address='VIA ROMA 1', zip_code='16100', country='ITALY', website='', notes='')
        
        models.Payment.objects.create(sender=models.Company.objects.get(name='ALFA'), receiver=models.Company.objects.get(name='MY COMPANY'), kind='ACTIVE', date='2019-03-10 11:16:09.184106+01:00', amount=1000, notes='TBA')
        
    def test_payment_set_up(self):
        alfa_payment = models.Payment.objects.get(sender=1)

        self.assertEqual(alfa_payment.amount, 1000)

    def test_payment_sender_label(self):
        obj = models.Payment.objects.get(id=1)
        field_label = obj._meta.get_field('sender').verbose_name
        
        self.assertEqual(field_label, 'sender')
                
    def test_payment_receiver_label(self):
        obj = models.Payment.objects.get(id=1)
        field_label = obj._meta.get_field('receiver').verbose_name
        
        self.assertEqual(field_label, 'receiver')
                
    def test_payment_kind_label(self):
        obj = models.Payment.objects.get(id=1)
        field_label = obj._meta.get_field('kind').verbose_name
        
        self.assertEqual(field_label, 'kind')
                
    def test_payment_date_label(self):
        obj = models.Payment.objects.get(id=1)
        field_label = obj._meta.get_field('date').verbose_name
        
        self.assertEqual(field_label, 'date')
                
    def test_payment_amount_label(self):
        obj = models.Payment.objects.get(id=1)
        field_label = obj._meta.get_field('amount').verbose_name
        
        self.assertEqual(field_label, 'amount')
                
    def test_payment_notes_label(self):
        obj = models.Payment.objects.get(id=1)
        field_label = obj._meta.get_field('notes').verbose_name
        
        self.assertEqual(field_label, 'notes')
            


# API test cases

class ApiTestCase(APITestCase):
    """Test connection to APIs"""
    def setUp(self):
        self.username = 'john_doe'
        self.password = 'foobar'
        self.user = User.objects.create(username=self.username, password=self.password)
        self.client.force_authenticate(user=self.user)
                
    def test_product_api_get(self):
        response = self.client.get('/api/v1/product/')
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
        
    
    
# Form test cases

class CompanyFormTestCase(TestCase):
    """Check correctness of Company form"""
    def test_product_form(self):
        form = forms.CompanyForm()
                
        self.assertEqual(form.fields['name'].label, 'Name')
        self.assertEqual(form.fields['vat_id'].label, 'Vat id')
        self.assertEqual(form.fields['industry'].label, 'Industry') 
        self.assertEqual(form.fields['city'].label, 'City')
        self.assertEqual(form.fields['address'].label, 'Address')
        self.assertEqual(form.fields['zip_code'].label, 'Zip code')
        self.assertEqual(form.fields['country'].label, 'Country')
        self.assertEqual(form.fields['website'].label, 'Website')
        self.assertEqual(form.fields['notes'].label, 'Notes')      
         
                
        
class ProductFormTestCase(TestCase):
    """Check correctness of Product form"""
    def test_product_form(self):
        form = forms.ProductForm()
                
        self.assertEqual(form.fields['name'].label, 'Name')
        self.assertEqual(form.fields['description'].label, 'Description')
        self.assertEqual(form.fields['quantity'].label, 'Quantity') 
        self.assertEqual(form.fields['price'].label, 'Price')
        self.assertEqual(form.fields['refill'].label, 'Refill')
        
        
        
class InvoiceFormTestCase(TestCase):
    """Check correctness of Invoice form"""
    def test_invoice_form(self):
        form = forms.InvoiceForm()
                
        self.assertEqual(form.fields['sender'].label, 'Sender')
        self.assertEqual(form.fields['receiver'].label, 'Receiver')
        self.assertEqual(form.fields['date'].label, 'Date') 
        self.assertEqual(form.fields['number'].label, 'Number')
        self.assertEqual(form.fields['amount'].label, 'Amount')
        self.assertEqual(form.fields['kind'].label, 'Kind')
        self.assertEqual(form.fields['product'].label, 'Product')
        self.assertEqual(form.fields['product_quantity'].label, 'Product quantity')
        self.assertEqual(form.fields['due_date'].label, 'Due date')
        self.assertEqual(form.fields['status'].label, 'Status')
        self.assertEqual(form.fields['notes'].label, 'Notes')
        
        
        
class PaymentFormTestCase(TestCase):
    """Check correctness of Invoice form"""
    def test_payment_form(self):
        form = forms.PaymentForm()
                
        self.assertEqual(form.fields['sender'].label, 'Sender')
        self.assertEqual(form.fields['receiver'].label, 'Receiver')
        self.assertEqual(form.fields['date'].label, 'Date') 
        self.assertEqual(form.fields['amount'].label, 'Amount')
        self.assertEqual(form.fields['kind'].label, 'Kind')
        self.assertEqual(form.fields['notes'].label, 'Notes')
       
     
     
# Views test cases

class MainViewTest(TestCase):
    """Test product views"""
    
    username = 'test_user'
    password = '!y6KD@HbEu4TZf'
    
    def setUp(self):
        test_user = User.objects.create_user(username=self.username, password=self.password)
        
        test_user.save()
        
        models.Company.objects.create(name='ALFA', vat_id='123456', industry='TECH', city='GENOVA', address='VIA ROMA 1', zip_code='16100', country='ITALY', website='', notes='')
        
    def test_redirect_if_not_logged(self):
        response = self.client.get(reverse('erp_core:product_list'))
        
        self.assertRedirects(response, '/login/?next=/product_list/')         
        
    def test_user_login(self):
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('erp_core:home'))
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_help_page(self):
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.get('/help/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
            
    def test_feature_page(self):
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.get('/feature/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_filtered_view_page(self):
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.get('/filtered_view/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)   
      


class CompanyViewTest(TestCase):
    """Test product views"""
    
    username = 'test_user'
    password = '!y6KD@HbEu4TZf'
    
    def setUp(self):
        test_user = User.objects.create_user(username=self.username, password=self.password)
        
        test_user.save()
        
        models.Company.objects.create(name='ALFA', vat_id='123456', industry='TECH', city='GENOVA', address='VIA ROMA 1', zip_code='16100', country='ITALY', website='', notes='')  
                
    def test_company_list(self):
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.get('/company_list/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_company_create_get(self):
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.get('/company_create/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_company_create_post(self):
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.post('/company_create/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_company_detail(self):
        login = self.client.login(username=self.username, password=self.password)
        obj_slug = models.Company.objects.get(id=1).vat_id
        response = self.client.get(f'/company_detail/{obj_slug}/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_company_update_get(self):
        login = self.client.login(username=self.username, password=self.password)
        obj_pk = models.Company.objects.get(id=1).id
        response = self.client.get(f'/company_update/{obj_pk}/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_company_update_post(self):
        login = self.client.login(username=self.username, password=self.password)
        obj_pk = models.Company.objects.get(id=1).id
        response = self.client.post(f'/company_update/{obj_pk}/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_company_clone_get(self):
        login = self.client.login(username=self.username, password=self.password)
        obj_pk = models.Company.objects.get(id=1).id
        response = self.client.get(f'/company_clone/{obj_pk}/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_company_clone_post(self):
        login = self.client.login(username=self.username, password=self.password)
        obj_pk = models.Company.objects.get(id=1).id
        response = self.client.post(f'/company_clone/{obj_pk}/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
                        
                
class ProductViewTest(TestCase):
    """Test product views"""
    
    username = 'test_user'
    password = '!y6KD@HbEu4TZf'
    
    def setUp(self):
        test_user = User.objects.create_user(username=self.username, password=self.password)
        
        test_user.save()
        
        models.Product.objects.create(name='ALFA', description='A PRODUCT', quantity='50', price='100', refill=True)
    
    def test_product_list(self):
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.get('/product_list/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_product_create_get(self):
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.get('/product_create/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_product_create_post(self):
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.post('/product_create/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_product_detail(self):
        login = self.client.login(username=self.username, password=self.password)
        obj_pk = models.Product.objects.get(id=1).id
        response = self.client.get(f'/product_detail/{obj_pk}/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_product_update_get(self):
        login = self.client.login(username=self.username, password=self.password)
        obj_pk = models.Product.objects.get(id=1).id
        response = self.client.get(f'/product_update/{obj_pk}/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_product_update_post(self):
        login = self.client.login(username=self.username, password=self.password)
        obj_pk = models.Product.objects.get(id=1).id
        response = self.client.post(f'/product_update/{obj_pk}/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_product_clone_get(self):
        login = self.client.login(username=self.username, password=self.password)
        obj_pk = models.Product.objects.get(id=1).id
        response = self.client.get(f'/product_clone/{obj_pk}/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_product_clone_post(self):
        login = self.client.login(username=self.username, password=self.password)
        obj_pk = models.Product.objects.get(id=1).id
        response = self.client.post(f'/product_clone/{obj_pk}/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
        
        
class InvoiceViewTest(TestCase):
    """Test invoice views"""
    
    username = 'test_user'
    password = '!y6KD@HbEu4TZf'
    
    def setUp(self):
        test_user = User.objects.create_user(username=self.username, password=self.password)
        
        test_user.save()
        
        models.Company.objects.create(name='ALFA', vat_id='123456', industry='TECH', city='GENOVA', address='VIA ROMA 1', zip_code='16100', country='ITALY', website='', notes='')
        
        models.Company.objects.create(name='MY COMPANY', vat_id='012345', industry='TECH', city='GENOVA', address='VIA ROMA 1', zip_code='16100', country='ITALY', website='', notes='')
        
        models.Product.objects.create(name='ALFA', description='A PRODUCT', quantity=50, price=100, refill=True)
        
        models.Invoice.objects.create(sender=models.Company.objects.get(name='ALFA'), receiver=models.Company.objects.get(name='MY COMPANY'), date='2019-03-10 11:16:09.184106+01:00', number='1', amount=1000, kind='ACTIVE', product=models.Product.objects.get(name='ALFA'), product_quantity=5, due_date='2019-03-10 11:16:09.184106+01:00', status='PAID', notes='')
    
    def test_invoice_list(self):
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.get('/invoice_list/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_invoice_create_get(self):
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.get('/invoice_create/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_invoice_create_post(self):
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.post('/invoice_create/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
                
    def test_invoice_update_post(self):
        login = self.client.login(username=self.username, password=self.password)
        obj_pk = models.Invoice.objects.get(id=1).id
        response = self.client.post(f'/invoice_update/{obj_pk}/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_invoice_clone_get(self):
        login = self.client.login(username=self.username, password=self.password)
        obj_pk = models.Invoice.objects.get(id=1).id
        response = self.client.get(f'/invoice_clone/{obj_pk}/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_invoice_clone_post(self):
        login = self.client.login(username=self.username, password=self.password)
        obj_pk = models.Invoice.objects.get(id=1).id
        response = self.client.post(f'/invoice_clone/{obj_pk}/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
        
    def test_invoice_active_overview(self):
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.get(f'/filtered_view/invoice_active/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    
    def test_invoice_active_overdue(self):
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.get(f'/filtered_view/invoice_active_overdue/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
        
    def test_invoice_passive_overview(self):
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.get(f'/filtered_view/invoice_passive/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    
    def test_invoice_passive_overdue(self):
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.get(f'/filtered_view/invoice_passive_overdue/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
        
    def test_invoice_check_active(self):
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.get(f'/filtered_view/check_active/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
        
    def test_invoice_check_passive(self):
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.get(f'/filtered_view/check_passive/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        


class PaymentViewTest(TestCase):
    """Test payment views"""
    
    username = 'test_user'
    password = '!y6KD@HbEu4TZf'
    
    def setUp(self):
        test_user = User.objects.create_user(username=self.username, password=self.password)
        
        test_user.save()
        
        models.Company.objects.create(name='ALFA', vat_id='123456', industry='TECH', city='GENOVA', address='VIA ROMA 1', zip_code='16100', country='ITALY', website='', notes='')
        
        models.Company.objects.create(name='MY COMPANY', vat_id='012345', industry='TECH', city='GENOVA', address='VIA ROMA 1', zip_code='16100', country='ITALY', website='', notes='')
        
        models.Payment.objects.create(sender=models.Company.objects.get(name='ALFA'), receiver=models.Company.objects.get(name='MY COMPANY'), kind='ACTIVE', date='2019-03-10 11:16:09.184106+01:00', amount=1000, notes='TBA')
    
    def test_payment_list(self):
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.get('/payment_list/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_payment_create_get(self):
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.get('/payment_create/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_payment_create_post(self):
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.post('/payment_create/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
                
    def test_payment_update_post(self):
        login = self.client.login(username=self.username, password=self.password)
        obj_pk = models.Payment.objects.get(id=1).id
        response = self.client.post(f'/payment_update/{obj_pk}/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_payment_clone_get(self):
        login = self.client.login(username=self.username, password=self.password)
        obj_pk = models.Payment.objects.get(id=1).id
        response = self.client.get(f'/payment_clone/{obj_pk}/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
    def test_payment_clone_post(self):
        login = self.client.login(username=self.username, password=self.password)
        obj_pk = models.Payment.objects.get(id=1).id
        response = self.client.post(f'/payment_clone/{obj_pk}/')
        
        self.assertEqual(login, True)
        self.assertEqual(response.status_code, 200)
        
        
        