from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.package.models.package import Course, Season, Lesson
from apps.package.serializers.package import CourseSerializer, SeasonSerializer, LessonSerializer


class CourseAdminAPIView(

    GenericAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin

):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CoursePublicAPIView(

    GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,

):

    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class SeasonAdminAPIView(

    GenericAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin

):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = SeasonSerializer
    queryset = Season.objects.all()


class SeasonPublicAPIView(

    GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,

):

    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = SeasonSerializer
    queryset = Season.objects.all()


class LessonAdminAPIView(

    GenericAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin

):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonPublicAPIView(

    GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,

):

    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()