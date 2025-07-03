from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from apps.products.models import Plates
from apps.categories.api.serializers import CategorySerializer  
from apps.categories.models import Category

class ProductSerializerPost(serializers.ModelSerializer):
    """
    Serializer for creating and updating Product (Plate) instances.
    Includes validation and custom price formatting in the response.
    """
    categories = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Category.objects.all()
    )

    class Meta:
        model = Plates
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative.")
        value = value * 10
        return value

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['price'] = data['price'] + ' €'
        return data

class ProductSerializerGet(TranslatableModelSerializer):
    """
    Serializer for reading Product (Plate) instances with related category info.
    Includes validation and custom price formatting in the response.
    """
    translations = TranslatedFieldsField(shared_model=Plates)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Plates
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['price'] = data['price'] + ' €'
        return data