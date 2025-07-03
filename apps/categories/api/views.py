from rest_framework import viewsets
from apps.categories.models import Category
from apps.categories.api.serializers import CategorySerializer
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.response import Response


@extend_schema_view(
    list=extend_schema(
        tags=['categories'],
        responses=CategorySerializer(many=True),
    ),
    create=extend_schema(
        tags=['categories'],
        request=CategorySerializer,
        responses={201: CategorySerializer, 400: Response({'detail': 'Invalid data'})},
    ),
    retrieve=extend_schema(
        tags=['categories'],
        responses={200: CategorySerializer, 404: Response({'detail': 'Not found'})},
    ),
    update=extend_schema(
        tags=['categories'],
        request=CategorySerializer,
        responses={200: CategorySerializer, 400: Response({'detail': 'Invalid data'})},
    ),
    partial_update=extend_schema(
        tags=['categories'],
        request=CategorySerializer,
        responses={200: CategorySerializer, 400: Response({'detail': 'Invalid data'})},
    ),
    destroy=extend_schema(
        tags=['categories'],
    ),
)
class CategoriesView(viewsets.ModelViewSet):
    """
    Viewset for managing categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]  
