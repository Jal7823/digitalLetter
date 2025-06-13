from rest_framework import serializers
from apps.company.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
        extra_kwargs = {
            'name': {'required': True, 'max_length': 100},
            'address': {'required': True, 'max_length': 200},
            'email': {'required': True, 'max_length': 100},
            'phone': {'required': True}
        }