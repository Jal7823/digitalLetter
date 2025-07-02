from rest_framework import serializers
from apps.company.models import Company
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField


class CompanySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Company)
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