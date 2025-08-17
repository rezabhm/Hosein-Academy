from rest_framework.routers import DefaultRouter

from apps.textbook.api.v1.view import TextBookAdminAPIView, TextBookPublicAPIView

router = DefaultRouter()

router.register('admin', TextBookAdminAPIView, basename='textbook-admin')
router.register('user', TextBookPublicAPIView, basename='textbook-user')

urlpatterns = router.urls
