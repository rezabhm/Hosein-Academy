from django.utils.decorators import method_decorator
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from apps.package.models.package import Course, Season, Lesson
from apps.package.serializers.package import CourseSerializer, SeasonSerializer, LessonSerializer
from .swagger_decorator import (
    admin_create_course_swagger,
    admin_retrieve_course_swagger,
    admin_update_course_swagger,
    admin_partial_update_course_swagger,
    admin_destroy_course_swagger,
    admin_list_course_swagger,
    public_retrieve_course_swagger,
    public_list_course_swagger,
    admin_create_season_swagger,
    admin_retrieve_season_swagger,
    admin_update_season_swagger,
    admin_partial_update_season_swagger,
    admin_destroy_season_swagger,
    admin_list_season_swagger,
    public_retrieve_season_swagger,
    public_list_season_swagger,
    admin_create_lesson_swagger,
    admin_retrieve_lesson_swagger,
    admin_update_lesson_swagger,
    admin_partial_update_lesson_swagger,
    admin_destroy_lesson_swagger,
    admin_list_lesson_swagger,
    public_retrieve_lesson_swagger,
    public_list_lesson_swagger,
)

@method_decorator(name='create', decorator=admin_create_course_swagger)
@method_decorator(name='retrieve', decorator=admin_retrieve_course_swagger)
@method_decorator(name='update', decorator=admin_update_course_swagger)
@method_decorator(name='partial_update', decorator=admin_partial_update_course_swagger)
@method_decorator(name='destroy', decorator=admin_destroy_course_swagger)
@method_decorator(name='list', decorator=admin_list_course_swagger)
class CourseAdminAPIView(ModelViewSet):
    """
    Admin-only API ViewSet for managing Course records.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

@method_decorator(name='retrieve', decorator=public_retrieve_course_swagger)
@method_decorator(name='list', decorator=public_list_course_swagger)
class CoursePublicAPIView(ReadOnlyModelViewSet):
    """
    Public API ViewSet for viewing Course records.
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

@method_decorator(name='create', decorator=admin_create_season_swagger)
@method_decorator(name='retrieve', decorator=admin_retrieve_season_swagger)
@method_decorator(name='update', decorator=admin_update_season_swagger)
@method_decorator(name='partial_update', decorator=admin_partial_update_season_swagger)
@method_decorator(name='destroy', decorator=admin_destroy_season_swagger)
@method_decorator(name='list', decorator=admin_list_season_swagger)
class SeasonAdminAPIView(ModelViewSet):
    """
    Admin-only API ViewSet for managing Season records.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = SeasonSerializer
    queryset = Season.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

@method_decorator(name='retrieve', decorator=public_retrieve_season_swagger)
@method_decorator(name='list', decorator=public_list_season_swagger)
class SeasonPublicAPIView(ReadOnlyModelViewSet):
    """
    Public API ViewSet for viewing Season records.
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = SeasonSerializer
    queryset = Season.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

@method_decorator(name='create', decorator=admin_create_lesson_swagger)
@method_decorator(name='retrieve', decorator=admin_retrieve_lesson_swagger)
@method_decorator(name='update', decorator=admin_update_lesson_swagger)
@method_decorator(name='partial_update', decorator=admin_partial_update_lesson_swagger)
@method_decorator(name='destroy', decorator=admin_destroy_lesson_swagger)
@method_decorator(name='list', decorator=admin_list_lesson_swagger)
class LessonAdminAPIView(ModelViewSet):
    """
    Admin-only API ViewSet for managing Lesson records.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

@method_decorator(name='retrieve', decorator=public_retrieve_lesson_swagger)
@method_decorator(name='list', decorator=public_list_lesson_swagger)
class LessonPublicAPIView(ReadOnlyModelViewSet):
    """
    Public API ViewSet for viewing Lesson records.
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']