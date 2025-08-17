from django.utils.decorators import method_decorator
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from apps.payment.models.payment import Transaction
from apps.payment.serializers.payment import PaymentSerializer
from .swagger_decorator import (
    admin_create_transaction_swagger,
    admin_retrieve_transaction_swagger,
    admin_update_transaction_swagger,
    admin_partial_update_transaction_swagger,
    admin_destroy_transaction_swagger,
    admin_list_transaction_swagger,
    user_retrieve_transaction_swagger,
    user_list_transaction_swagger,
)


@method_decorator(name='create', decorator=admin_create_transaction_swagger)
@method_decorator(name='retrieve', decorator=admin_retrieve_transaction_swagger)
@method_decorator(name='update', decorator=admin_update_transaction_swagger)
@method_decorator(name='partial_update', decorator=admin_partial_update_transaction_swagger)
@method_decorator(name='destroy', decorator=admin_destroy_transaction_swagger)
@method_decorator(name='list', decorator=admin_list_transaction_swagger)
class TransactionAdminAPIView(ModelViewSet):
    """
    Admin-only API ViewSet for managing Transaction records.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = PaymentSerializer
    queryset = Transaction.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username']


@method_decorator(name='retrieve', decorator=user_retrieve_transaction_swagger)
@method_decorator(name='list', decorator=user_list_transaction_swagger)
class TransactionUserAPIView(ReadOnlyModelViewSet):
    """
    Authenticated user API ViewSet for viewing own Transaction records.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentSerializer

    def get_queryset(self):
        """
        Restrict queryset to the authenticated user's transactions.
        """
        return Transaction.objects.filter(user=self.request.user)