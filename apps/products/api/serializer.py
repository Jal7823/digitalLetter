from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from apps.products.models import Plates
from apps.categories.api.serializers import CategorySerializerGet, CategorySerializerPost
from apps.categories.models import Category


class ProductSerializerPost(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Plates)
    categories = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Category.objects.all()
    )

    class Meta:
        model = Plates
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def create(self, validated_data):
        translations = validated_data.pop('translations', {})
        categories = validated_data.pop('categories', [])
        instance = Plates.objects.create(**validated_data)
        instance.categories.set(categories)
        for lang_code, translation_fields in translations.items():
            instance.set_current_language(lang_code)
            for attr, value in translation_fields.items():
                setattr(instance, attr, value)
            instance.save()
        return instance

    def update(self, instance, validated_data):
        translations = validated_data.pop('translations', {})
        categories = validated_data.pop('categories', None)
        if categories is not None:
            instance.categories.set(categories)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        for lang_code, translation_fields in translations.items():
            instance.set_current_language(lang_code)
            for attr, value in translation_fields.items():
                setattr(instance, attr, value)
        instance.save()
        return instance


class ProductSerializerGet(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Plates)
    categories = CategorySerializerGet(many=True, read_only=True)  # 👈 aquí lo cambiamos

    class Meta:
        model = Plates
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['price'] = data['price'] + ' €'
        return data
