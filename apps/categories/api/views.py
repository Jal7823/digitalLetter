from rest_framework import viewsets
from apps.categories.models import Category
from apps.categories.api.serializers import CategorySerializer
from rest_framework.permissions import AllowAny


class CategoriesView(viewsets.ModelViewSet):
    """
    Viewset for managing categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]  # Adjust permissions as needed

