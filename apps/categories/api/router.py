from rest_framework.routers import DefaultRouter
from apps.categories.api.views import CategoriesView


router = DefaultRouter()
router.register(r'categories', CategoriesView, basename='categories')
urlpatterns = router.urls