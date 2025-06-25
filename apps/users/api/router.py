from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.users.api.views import RegisterClients, RegisterEmploye,UsersListViewSet, MeView, ChangePasswordView

router = DefaultRouter()
router.register(r'employe', RegisterEmploye, basename='employe')
router.register(r'clients', RegisterClients, basename='clients')
router.register(r'users-list', UsersListViewSet, basename='users-list')


urlpatterns = [
    path('', include(router.urls)),
    path('me/', MeView.as_view(), name='me'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),

]