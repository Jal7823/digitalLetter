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

    def create(self, validated_data):
        translations = validated_data.pop('translations', {})
        instance = Company.objects.create(**validated_data)
        for lang_code, fields in translations.items():
            instance.set_current_language(lang_code)
            for attr, value in fields.items():
                setattr(instance, attr, value)
            instance.save()
        return instance

    def update(self, instance, validated_data):
        translations = validated_data.pop('translations', {})
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        for lang_code, fields in translations.items():
            instance.set_current_language(lang_code)
            for attr, value in fields.items():
                setattr(instance, attr, value)
        instance.save()
        return instance
