from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.package.models.insights import Category, FAQ, Comment
from apps.package.serializers.insights import CategorySerializer, FAQSerializer, CommentSerializer
from apps.textbook.models import TextBook
from apps.textbook.serializers import TextBookSerializer


class TextBookAdminAPIView(

    GenericAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin

):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = TextBookSerializer
    queryset = TextBook.objects.all()


class TextBookPublicAPIView(

    GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,

):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TextBookSerializer
    queryset = TextBook.objects.all()

