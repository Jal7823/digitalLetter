from rest_framework.routers import DefaultRouter
from apps.company.api.views import CompanyView

router = DefaultRouter()
router.register(r'company', CompanyView, basename='company')

urlpatterns = router.urls