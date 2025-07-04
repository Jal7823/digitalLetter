from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from rest_framework import serializers
from apps.categories.models import Category

# Serializer para GET (leer)
class CategorySerializerGet(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Category)

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

# Serializer para POST/PUT/PATCH (escribir)
class CategorySerializerPost(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def create(self, validated_data):
        translations = validated_data.pop('translations', {})
        instance = Category.objects.create(**validated_data)
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
