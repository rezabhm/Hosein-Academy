from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.package.models.insights import Category, FAQ, Comment
from apps.package.serializers.insights import CategorySerializer, FAQSerializer, CommentSerializer


class CategoryAdminAPIView(

    GenericAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin

):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryPublicAPIView(

    GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,

):

    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class FAQAdminAPIView(

    GenericAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin

):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()


class FAQPublicAPIView(

    GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,

):

    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()


class CommentAdminAPIView(

    GenericAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin

):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentPublicAPIView(

    GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,

):

    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
