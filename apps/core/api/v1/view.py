from django.utils.decorators import method_decorator
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from apps.core.models import StudentInformation, Teacher
from apps.core.serializers import StudentInformationSerializer, TeacherSerializer
from .swagger_decorator import (
    admin_create_student_info_swagger,
    admin_retrieve_student_info_swagger,
    admin_update_student_info_swagger,
    admin_partial_update_student_info_swagger,
    admin_destroy_student_info_swagger,
    admin_list_student_info_swagger,
    user_retrieve_student_info_swagger,
    user_list_student_info_swagger,
    admin_create_teacher_swagger,
    admin_retrieve_teacher_swagger,
    admin_update_teacher_swagger,
    admin_partial_update_teacher_swagger,
    admin_destroy_teacher_swagger,
    admin_list_teacher_swagger,
    public_retrieve_teacher_swagger,
    public_list_teacher_swagger,
)


@method_decorator(name='create', decorator=admin_create_student_info_swagger)
@method_decorator(name='retrieve', decorator=admin_retrieve_student_info_swagger)
@method_decorator(name='update', decorator=admin_update_student_info_swagger)
@method_decorator(name='partial_update', decorator=admin_partial_update_student_info_swagger)
@method_decorator(name='destroy', decorator=admin_destroy_student_info_swagger)
@method_decorator(name='list', decorator=admin_list_student_info_swagger)
class StudentInformationAdminAPIView(ModelViewSet):
    """
    Admin-only API ViewSet for managing StudentInformation records.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = StudentInformationSerializer
    queryset = StudentInformation.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username']


@method_decorator(name='retrieve', decorator=user_retrieve_student_info_swagger)
@method_decorator(name='list', decorator=user_list_student_info_swagger)
class StudentInformationUserAPIView(ReadOnlyModelViewSet):
    """
    Authenticated user API ViewSet for viewing own StudentInformation records.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StudentInformationSerializer

    def get_queryset(self):
        """
        Restrict queryset to the authenticated user's student information.
        """
        return StudentInformation.objects.filter(user=self.request.user)


@method_decorator(name='create', decorator=admin_create_teacher_swagger)
@method_decorator(name='retrieve', decorator=admin_retrieve_teacher_swagger)
@method_decorator(name='update', decorator=admin_update_teacher_swagger)
@method_decorator(name='partial_update', decorator=admin_partial_update_teacher_swagger)
@method_decorator(name='destroy', decorator=admin_destroy_teacher_swagger)
@method_decorator(name='list', decorator=admin_list_teacher_swagger)
class TeacherAdminAPIView(ModelViewSet):
    """
    Admin-only API ViewSet for managing Teacher records.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username']


@method_decorator(name='retrieve', decorator=public_retrieve_teacher_swagger)
@method_decorator(name='list', decorator=public_list_teacher_swagger)
class TeacherPublicAPIView(ReadOnlyModelViewSet):
    """
    Public API ViewSet for viewing Teacher records.
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username']
