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
            