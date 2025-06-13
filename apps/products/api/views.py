from rest_framework import viewsets
from rest_framework.permissions import AllowAny 
from apps.products.models import Plates
from apps.products.api.serializer import ProductSerializerPost, ProductSerializerGet


class ProductsViewSetGet(viewsets.ModelViewSet):
    queryset = Plates.objects.filter(available=True)
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProductSerializerGet
        return ProductSerializerPost