from rest_framework import viewsets
from rest_framework.permissions import AllowAny 
from apps.products.models import Plates
from apps.products.api.serializer import ProductSerializerPost, ProductSerializerGet
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.response import Response

@extend_schema_view(
    list=extend_schema(
        tags=['plates'],
        responses=ProductSerializerGet(many=True),
    ),
    create=extend_schema(
        tags=['plates'],
        request=ProductSerializerPost,
        responses={201: ProductSerializerGet, 400: Response({'detail': 'Invalid data'})},
    ),
    retrieve=extend_schema(
        tags=['plates'],
        responses={200: ProductSerializerGet, 404: Response({'detail': 'Not found'})},
    ),
    update=extend_schema(
        tags=['plates'],
        request=ProductSerializerPost,
        responses={200: ProductSerializerGet, 400: Response({'detail': 'Invalid data'})},
    ),
    partial_update=extend_schema(
        tags=['plates'],
        request=ProductSerializerPost,
        responses={200: ProductSerializerGet, 400: Response({'detail': 'Invalid data'})},
    ),
    destroy=extend_schema(
        tags=['plates'],
    ),
)
class ProductsViewSetGet(viewsets.ModelViewSet):
    queryset = Plates.objects.filter(available=True)
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProductSerializerGet
        return ProductSerializerPost