from enum import Enum
from django.db import models


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]
    
class Company(models.Model):
    """Manage company profile and their attributes"""   
    
    class Industry(ChoiceEnum):
        """Create industry choices"""
        ENERGY = 'Energy'
        RETAIL = 'Retail'
        TECH = 'Tech'
        OTHER = 'Other'
         
    name = models.CharField(max_length=100)
    vat_id = models.CharField(max_length=15, unique=True, blank=True, null=True)
    industry = models.CharField(max_length=15, choices=Industry.choices(), default=Industry.choices()[0][0])
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    zip_code =  models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    website = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name.upper()
    
class Invoice(models.Model):
    """Manage invoice and their attributes"""
    
    class Kind(ChoiceEnum):
        """Create invoice statuses"""
        ACTIVE = 'Active'
        PASSIVE = 'Passive'
        CREDIT = 'Credit Note'
    
    class Status(ChoiceEnum):
        PAID = "Paid"
        UNPAID = "Unpaid"
        
    sender = models.ForeignKey(Company, related_name="invoice_sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(Company, related_name="invoice_receiver", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=False)
    number = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    kind = models.CharField(max_length=10, choices=Kind.choices(), default=Kind.choices()[0][0])
    due_date = models.DateTimeField(auto_now_add=False)
    status = models.CharField(max_length=10, choices=Status.choices(), default=Status.choices()[0][0])
    notes = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return f"Sender: {self.sender}, Receiver:{self.receiver}, Amount:{self.amount}, Due_date:{self.due_date}"  
    
class Payment(models.Model):
    """Manage incoming and outcoming payments"""
    
    class Kind(ChoiceEnum):
        """Create payment statuses"""
        ACTIVE = 'Active'
        PASSIVE = 'Passive'
    
    sender = models.ForeignKey(Company, related_name="payment_sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(Company, related_name="payment_receiver", on_delete=models.CASCADE)
    kind = models.CharField(max_length=10, choices=Kind.choices(), default=Kind.choices()[0][0])
    date = models.DateTimeField(auto_now_add=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return f"{self.sender}, {self.amount}"

# wip    
class Item(models.Model):
    """Manage physical goods management"""
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    refill = models.BooleanField(default=False)
    
    
    