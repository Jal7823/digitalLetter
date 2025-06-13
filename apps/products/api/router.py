from rest_framework.routers import DefaultRouter
from apps.products.api.views import ProductsViewSetGet

router = DefaultRouter()
router.register(r'products', ProductsViewSetGet, basename='products')


urlpatterns = router.urls
