from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.core.api.v1.auth_view import SendOtpView, RefreshTokenView, LogoutView, VerifyOtpView
from apps.core.api.v1.view import StudentInformationAdminAPIView, StudentInformationUserAPIView, TeacherPublicAPIView, \
    TeacherAdminAPIView

router = DefaultRouter()

router.register('admin/student-information', StudentInformationAdminAPIView, basename='admin-student-information')
router.register('user/student-information', StudentInformationUserAPIView, basename='user-student-information')

router.register('admin/teacher', TeacherAdminAPIView, basename='admin-teacher')
router.register('user/teacher', TeacherPublicAPIView, basename='user-teacher')

urlpatterns = [
    path('auth/send-otp/', SendOtpView.as_view(), name='send_otp'),
    path('auth/verify-otp/', VerifyOtpView.as_view(), name='verify_otp'),
    path('auth/refresh-token/', RefreshTokenView.as_view(), name='refresh_token'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
]

urlpatterns += router.urls
