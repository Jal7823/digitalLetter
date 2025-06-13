from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.users.api.views import RegisterClients, RegisterEmploye

router = DefaultRouter()
router.register(r'employe', RegisterEmploye, basename='employe')
router.register(r'clients', RegisterClients, basename='clients')

urlpatterns = [
    path('', include(router.urls)),
]