from rest_framework.routers import DefaultRouter

from apps.package.api.v1.insights.view import CategoryAdminAPIView, FAQAdminAPIView, FAQPublicAPIView, \
    CommentAdminAPIView, CommentPublicAPIView, CategoryPublicAPIView
from apps.package.api.v1.package.view import CourseAdminAPIView, CoursePublicAPIView, SeasonAdminAPIView, \
    SeasonPublicAPIView, LessonPublicAPIView, LessonAdminAPIView

router = DefaultRouter()

# package apis
router.register('admin/course', CourseAdminAPIView, basename='admin-course')
router.register('public/course', CoursePublicAPIView, basename='public-course')

router.register('admin/season', SeasonAdminAPIView, basename='admin-season')
router.register('public/season', SeasonPublicAPIView, basename='public-season')

router.register('admin/lesson', LessonAdminAPIView, basename='admin-lesson')
router.register('public/lesson', LessonPublicAPIView, basename='public-lesson')

# insights apis
router.register('admin/category', CategoryAdminAPIView, basename='admin-category')
router.register('public/category', CategoryPublicAPIView, basename='public-category')

router.register('admin/faq', FAQAdminAPIView, basename='admin-faq')
router.register('public/faq', FAQPublicAPIView, basename='public-faq')

router.register('admin/comment', CommentAdminAPIView, basename='admin-comment')
router.register('public/comment', CommentPublicAPIView, basename='public-comment')


urlpatterns = router.urls
