from rest_framework import viewsets
from apps.categories.models import Category
from apps.categories.api.serializers import CategorySerializerGet, CategorySerializerPost
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.response import Response

class CategoriesView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CategorySerializerGet
        return CategorySerializerPost

    def get_serializer(self, *args, **kwargs):
        # Para respuestas de create/update/partial_update usamos serializer GET para que incluya translations
        if self.action in ['create', 'update', 'partial_update']:
            kwargs.setdefault('context', self.get_serializer_context())
            return CategorySerializerGet(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)
