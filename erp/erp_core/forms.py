from django import forms

from . import models


class CompanyForm(forms.ModelForm):
    """Manage company creations"""
    class Meta:
        model = models.Company
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'label': 'Company Name',
                'class': 'form-control',
                'name': 'name',
                'id': 'name',
                'placeholder': 'Enter company name',
                'required': True,
                },
            ),
            'vat_id': forms.TextInput(attrs={
                'label': 'Vat Id',
                'class': 'form-control',
                'name': 'vat_id',
                'id': 'vat_id',
                'placeholder': 'Enter vat id',
                'required': False,
                },
            ),
            'industry': forms.Select(attrs={
                'label': 'Industry',
                'class': 'form-control',
                'name': 'industry',
                'id': 'industry',
                'placeholder': 'Enter industry',
                'required': True,
                },
            ),
            'city': forms.TextInput(attrs={
                'label': 'City',
                'class': 'form-control',
                'name': 'city',
                'id': 'city',
                'placeholder': 'Enter city',
                'required': True,
                },
            ),
            'address': forms.TextInput(attrs={
                'label': 'Address',
                'class': 'form-control',
                'name': 'address',
                'id': 'address',
                'placeholder': 'Enter address',
                'required': True,
                },
            ),
            'zip_code': forms.TextInput(attrs={
                'label': 'Zip code',
                'class': 'form-control',
                'name': 'zip_code',
                'id': 'zip_code',
                'placeholder': 'Enter zip code',
                'required': True,
                },
            ),
            'country': forms.TextInput(attrs={
                'label': 'Country',
                'class': 'form-control',
                'name': 'country',
                'id': 'country',
                'placeholder': 'Enter country',
                'required': True,
                },
            ),
            'website': forms.URLInput(attrs={
                'label': 'Website',
                'class': 'form-control',
                'name': 'website',
                'id': 'website',
                'placeholder': 'https://www.example.com',
                'required': False,
                },
            ),
            'notes': forms.Textarea(attrs={
                'label': 'Notes',
                'class': 'form-control',
                'name': 'notes',
                'id': 'notes',
                'rows': 2, 
                'cols': 10, 
                'placeholder': 'Additional notes',
                'required': False,
                },
            ),
        }
        
        
class ProductForm(forms.ModelForm):
    """Manage product creation"""
    class Meta:
        model = models.Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'label': 'Product Name',
                'class': 'form-control',
                'name': 'product_name',
                'id': 'product_name',
                'placeholder': 'Enter product name',
                'required': True,
                },
            ),
            'description': forms.Textarea(attrs={
                'label': 'Product Description',
                'class': 'form-control',
                'name': 'product_description',
                'id': 'product_description',
                'rows': 2, 
                'cols': 10, 
                'placeholder': 'Enter product description',
                'required': False,
                },
            ),
            'quantity': forms.NumberInput(attrs={
                'label': 'Product Quantity',
                'class': 'form-control',
                'name': 'product_quantity',
                'id': 'product_quantity',
                'placeholder': '5',
                'required': True,
                },
            ),
             'price': forms.NumberInput(attrs={
                'label': 'Product Price',
                'class': 'form-control',
                'name': 'product_price',
                'id': 'product_price',
                'placeholder': '100',
                'required': False,
                },
            ),
            'refill': forms.CheckboxInput(attrs={
                'name': 'refill',
                'id': 'refill',
                'required': False,
                },
            ),
        }    
        
        
class InvoiceForm(forms.ModelForm):
    """Manage invoice creation"""
    class Meta:
        model = models.Invoice
        fields = '__all__'
        widgets = {
            'sender': forms.Select(attrs={
                'label': 'Sender',
                'class': 'form-control',
                'name': 'sender',
                'id': 'sender',
                'placeholder': 'Enter sender name',
                'required': True,
                },
            ),
            'receiver': forms.Select(attrs={
                'label': 'Receiver',
                'class': 'form-control',
                'name': 'receiver',
                'id': 'receiver',
                'placeholder': 'Enter receiver name',
                'required': True,
                },
            ),
            'date': forms.DateInput(attrs={
                'label': 'Emission Date',
                'class': 'form-control',
                'name': 'date',
                'id': 'date',
                'placeholder': 'dd/mm/yyyy',
                'required': True,
                },
            ),
            'number': forms.NumberInput(attrs={
                'label': 'Invoice Number',
                'class': 'form-control',
                'name': 'number',
                'id': 'number',
                'placeholder': 'Enter invoice number',
                'required': True,
                },
            ),
            'amount': forms.NumberInput(attrs={
                'label': 'Invoice Amount',
                'class': 'form-control',
                'name': 'amount',
                'id': 'amount',
                'placeholder': 'Enter amount in euros, ex: 5000,12',
                'required': True,
                },
            ),
            'kind': forms.Select(attrs={
                'label': 'Invoice Type',
                'class': 'form-control',
                'name': 'kind',
                'id': 'kind',
                'placeholder': 'Enter invoice type',
                'required': True,
                },
            ),
            'product': forms.Select(attrs={
                'label': 'Product',
                'class': 'form-control',
                'name': 'product',
                'id': 'product',
                'placeholder': 'Enter product name',
                'required': True,
                },
            ),
            'product_quantity': forms.NumberInput(attrs={
                'label': 'Product Quantity',
                'class': 'form-control',
                'name': 'product_quantity',
                'id': 'product_quantity',
                'placeholder': '5',
                'required': False,
                },
            ),
            'due_date': forms.DateInput(attrs={
                'label': 'Invoice Due Date',
                'class': 'form-control',
                'name': 'due_date',
                'id': 'due_date',
                'placeholder': 'dd/mm/yyyy',
                'required': True,
                },
            ),
            'status': forms.Select(attrs={
                'label': 'Invoice Status',
                'class': 'form-control',
                'name': 'status',
                'id': 'status',
                'placeholder': 'Enter invoice status',
                'required': True,
                },
            ),
            'notes': forms.Textarea(attrs={
                'label': 'Notes',
                'class': 'form-control',
                'name': 'notes',
                'id': 'notes',
                'rows': 2, 
                'cols': 10, 
                'placeholder': 'Additional notes',
                'required': False,
                },
            ),
        }         
        
        
class PaymentForm(forms.ModelForm):
    """Manage payment creation"""
    class Meta:
        model = models.Payment
        fields = '__all__'
        widgets = {
            'sender': forms.Select(attrs={
                'label': 'Sender',
                'class': 'form-control',
                'name': 'sender',
                'id': 'sender',
                'placeholder': 'Enter sender name',
                'required': True,
                },
            ),
            'receiver': forms.Select(attrs={
                'label': 'Receiver',
                'class': 'form-control',
                'name': 'receiver',
                'id': 'receiver',
                'placeholder': 'Enter receiver name',
                'required': True,
                },
            ),
            'date': forms.DateInput(attrs={
                'label': 'Emission Date',
                'class': 'form-control',
                'name': 'date',
                'id': 'date',
                'placeholder': 'dd/mm/yyyy',
                'required': True,
                },
            ),
            'amount': forms.NumberInput(attrs={
                'label': 'Invoice Amount',
                'class': 'form-control',
                'name': 'amount',
                'id': 'amount',
                'placeholder': 'Enter amount in euros, ex: 5000,12',
                'required': True,
                },
            ),
            'kind': forms.Select(attrs={
                'label': 'Invoice Type',
                'class': 'form-control',
                'name': 'kind',
                'id': 'kind',
                'placeholder': 'Enter invoice type',
                'required': True,
                },
            ),
            'notes': forms.Textarea(attrs={
                'label': 'Notes',
                'class': 'form-control',
                'name': 'notes',
                'id': 'notes',
                'rows': 2, 
                'cols': 10, 
                'placeholder': 'Additional notes',
                'required': False,
                },
            ),
        }
              