from rest_framework import viewsets
from apps.company.models import Company
from apps.company.api.serializers import CompanySerializer

class CompanyView(viewsets.ModelViewSet):
    """
    ViewSet for Company model.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
