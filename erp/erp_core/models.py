from enum import Enum
from django.db import models

# https://notestoself.dev/posts/django-field-choices-inner-class-enum/
class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]
    
class Company(models.Model):
    """Create company profile and their attributes"""
    class Meta:
        verbose_name_plural = "Companies"
    
    class Industry(ChoiceEnum):
        """Create industry choices"""
        ENERGY = 'Energy'
        RETAIL = 'Retail'
        TECH = 'Tech'
        OTHER = 'Other'
         
    name = models.CharField(max_length=100)
    vat_id = models.CharField(max_length=15, unique=True, blank=True, null=True)
    industry = models.CharField(max_length=15, choices=Industry.choices(), default=Industry.TECH)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    zip_code =  models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    website = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name.upper()
    





"""
azienda (nome, partita iva, settore, città, indirizzo, cap, provincia, nazione, sito web, note)
fattura (emittente, destinatario, data, numero, importo, tipologia di fattura, scadenza, stato pagamento, note)
"""
