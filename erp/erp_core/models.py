from django.db import models

class Company(models.Model):
    """Create company profile and their attributes"""
    name = models.CharField(max_length=100)
    vat_id = models.CharField(max_length=15, unique=True, blank=True, null=True)






"""
azienda (nome, partita iva, settore, città, indirizzo, cap, provincia, nazione, sito web, note)
fattura (emittente, destinatario, data, numero, importo, tipologia di fattura, scadenza, stato pagamento, note)
"""
