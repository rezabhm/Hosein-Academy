from django.utils.decorators import method_decorator
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from apps.package.models.insights import Category, FAQ, Comment
from apps.package.serializers.insights import CategorySerializer, FAQSerializer, CommentSerializer
from .swagger_decorator import (
    admin_create_category_swagger,
    admin_retrieve_category_swagger,
    admin_update_category_swagger,
    admin_partial_update_category_swagger,
    admin_destroy_category_swagger,
    admin_list_category_swagger,
    public_retrieve_category_swagger,
    public_list_category_swagger,
    admin_create_faq_swagger,
    admin_retrieve_faq_swagger,
    admin_update_faq_swagger,
    admin_partial_update_faq_swagger,
    admin_destroy_faq_swagger,
    admin_list_faq_swagger,
    public_retrieve_faq_swagger,
    public_list_faq_swagger,
    admin_create_comment_swagger,
    admin_retrieve_comment_swagger,
    admin_update_comment_swagger,
    admin_partial_update_comment_swagger,
    admin_destroy_comment_swagger,
    admin_list_comment_swagger,
    public_retrieve_comment_swagger,
    public_list_comment_swagger,
)


@method_decorator(name='create', decorator=admin_create_category_swagger)
@method_decorator(name='retrieve', decorator=admin_retrieve_category_swagger)
@method_decorator(name='update', decorator=admin_update_category_swagger)
@method_decorator(name='partial_update', decorator=admin_partial_update_category_swagger)
@method_decorator(name='destroy', decorator=admin_destroy_category_swagger)
@method_decorator(name='list', decorator=admin_list_category_swagger)
class CategoryAdminAPIView(ModelViewSet):
    """
    Admin-only API ViewSet for managing Category records.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


@method_decorator(name='retrieve', decorator=public_retrieve_category_swagger)
@method_decorator(name='list', decorator=public_list_category_swagger)
class CategoryPublicAPIView(ReadOnlyModelViewSet):
    """
    Public API ViewSet for viewing Category records.
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


@method_decorator(name='create', decorator=admin_create_faq_swagger)
@method_decorator(name='retrieve', decorator=admin_retrieve_faq_swagger)
@method_decorator(name='update', decorator=admin_update_faq_swagger)
@method_decorator(name='partial_update', decorator=admin_partial_update_faq_swagger)
@method_decorator(name='destroy', decorator=admin_destroy_faq_swagger)
@method_decorator(name='list', decorator=admin_list_faq_swagger)
class FAQAdminAPIView(ModelViewSet):
    """
    Admin-only API ViewSet for managing FAQ records.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['question']


@method_decorator(name='retrieve', decorator=public_retrieve_faq_swagger)
@method_decorator(name='list', decorator=public_list_faq_swagger)
class FAQPublicAPIView(ReadOnlyModelViewSet):
    """
    Public API ViewSet for viewing FAQ records.
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['question']


@method_decorator(name='create', decorator=admin_create_comment_swagger)
@method_decorator(name='retrieve', decorator=admin_retrieve_comment_swagger)
@method_decorator(name='update', decorator=admin_update_comment_swagger)
@method_decorator(name='partial_update', decorator=admin_partial_update_comment_swagger)
@method_decorator(name='destroy', decorator=admin_destroy_comment_swagger)
@method_decorator(name='list', decorator=admin_list_comment_swagger)
class CommentAdminAPIView(ModelViewSet):
    """
    Admin-only API ViewSet for managing Comment records.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['content']


@method_decorator(name='retrieve', decorator=public_retrieve_comment_swagger)
@method_decorator(name='list', decorator=public_list_comment_swagger)
class CommentPublicAPIView(ReadOnlyModelViewSet):
    """
    Public API ViewSet for viewing Comment records.
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['content']