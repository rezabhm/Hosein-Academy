from django.utils.decorators import method_decorator
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from apps.textbook.models import TextBook
from apps.textbook.serializers import TextBookSerializer
from .swagger_decorator import (
    admin_create_textbook_swagger,
    admin_retrieve_textbook_swagger,
    admin_update_textbook_swagger,
    admin_partial_update_textbook_swagger,
    admin_destroy_textbook_swagger,
    admin_list_textbook_swagger,
    user_retrieve_textbook_swagger,
    user_list_textbook_swagger,
)


@method_decorator(name='create', decorator=admin_create_textbook_swagger)
@method_decorator(name='retrieve', decorator=admin_retrieve_textbook_swagger)
@method_decorator(name='update', decorator=admin_update_textbook_swagger)
@method_decorator(name='partial_update', decorator=admin_partial_update_textbook_swagger)
@method_decorator(name='destroy', decorator=admin_destroy_textbook_swagger)
@method_decorator(name='list', decorator=admin_list_textbook_swagger)
class TextBookAdminAPIView(ModelViewSet):
    """
    Admin-only API ViewSet for managing TextBook records.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = TextBookSerializer
    queryset = TextBook.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


@method_decorator(name='retrieve', decorator=user_retrieve_textbook_swagger)
@method_decorator(name='list', decorator=user_list_textbook_swagger)
class TextBookPublicAPIView(ReadOnlyModelViewSet):
    """
    Authenticated user API ViewSet for viewing TextBook records.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TextBookSerializer
    queryset = TextBook.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']