from rest_framework import serializers
from . import models


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    """
    API endpoint that allows groups to be viewed via hyperlink.
    """
    url = serializers.HyperlinkedIdentityField(view_name='erp_core:company-detail')
    class Meta:
        model = models.Company
        fields = '__all__'

        
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    API endpoint that allows groups to be viewed via hyperlink.
    """
    url = serializers.HyperlinkedIdentityField(view_name='erp_core:product-detail')
    class Meta:
        model = models.Product
        fields = '__all__'

        
class InvoiceSerializer(serializers.ModelSerializer):
    """
    API endpoint that allows groups to be viewed via hyperlink.
    """
    url = serializers.HyperlinkedIdentityField(view_name='erp_core:invoice-detail')
    class Meta:
        model = models.Invoice
        fields = '__all__'

        
class PaymentSerializer(serializers.ModelSerializer):
    """
    API endpoint that allows groups to be viewed via hyperlink.
    """
    url = serializers.HyperlinkedIdentityField(view_name='erp_core:payment-detail')
    class Meta:
        model = models.Payment
        fields = '__all__'
    