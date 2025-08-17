from django.utils.decorators import method_decorator
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from apps.payment.models.subscription import Subscription, InstallmentPayment, ImmediatePayment
from apps.payment.serializers.subscription import SubscriptionSerializer, InstallmentPaymentSerializer, ImmediatePaymentSerializer
from .swagger_decorator import (
    admin_create_subscription_swagger,
    admin_retrieve_subscription_swagger,
    admin_update_subscription_swagger,
    admin_partial_update_subscription_swagger,
    admin_destroy_subscription_swagger,
    admin_list_subscription_swagger,
    user_retrieve_subscription_swagger,
    user_list_subscription_swagger,
    admin_create_installment_payment_swagger,
    admin_retrieve_installment_payment_swagger,
    admin_update_installment_payment_swagger,
    admin_partial_update_installment_payment_swagger,
    admin_destroy_installment_payment_swagger,
    admin_list_installment_payment_swagger,
    user_retrieve_installment_payment_swagger,
    user_list_installment_payment_swagger,
    admin_create_immediate_payment_swagger,
    admin_retrieve_immediate_payment_swagger,
    admin_update_immediate_payment_swagger,
    admin_partial_update_immediate_payment_swagger,
    admin_destroy_immediate_payment_swagger,
    admin_list_immediate_payment_swagger,
    user_retrieve_immediate_payment_swagger,
    user_list_immediate_payment_swagger,
)

@method_decorator(name='create', decorator=admin_create_subscription_swagger)
@method_decorator(name='retrieve', decorator=admin_retrieve_subscription_swagger)
@method_decorator(name='update', decorator=admin_update_subscription_swagger)
@method_decorator(name='partial_update', decorator=admin_partial_update_subscription_swagger)
@method_decorator(name='destroy', decorator=admin_destroy_subscription_swagger)
@method_decorator(name='list', decorator=admin_list_subscription_swagger)
class SubscriptionAdminAPIView(ModelViewSet):
    """
    Admin-only API ViewSet for managing Subscription records.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username']


@method_decorator(name='retrieve', decorator=user_retrieve_subscription_swagger)
@method_decorator(name='list', decorator=user_list_subscription_swagger)
class SubscriptionUserAPIView(ReadOnlyModelViewSet):
    """
    Authenticated user API ViewSet for viewing own Subscription records.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        """
        Restrict queryset to the authenticated user's subscriptions.
        """
        return Subscription.objects.filter(user=self.request.user)


@method_decorator(name='create', decorator=admin_create_installment_payment_swagger)
@method_decorator(name='retrieve', decorator=admin_retrieve_installment_payment_swagger)
@method_decorator(name='update', decorator=admin_update_installment_payment_swagger)
@method_decorator(name='partial_update', decorator=admin_partial_update_installment_payment_swagger)
@method_decorator(name='destroy', decorator=admin_destroy_installment_payment_swagger)
@method_decorator(name='list', decorator=admin_list_installment_payment_swagger)
class InstallmentPaymentAdminAPIView(ModelViewSet):
    """
    Admin-only API ViewSet for managing InstallmentPayment records.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = InstallmentPaymentSerializer
    queryset = InstallmentPayment.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username']


@method_decorator(name='retrieve', decorator=user_retrieve_installment_payment_swagger)
@method_decorator(name='list', decorator=user_list_installment_payment_swagger)
class InstallmentPaymentUserAPIView(ReadOnlyModelViewSet):
    """
    Authenticated user API ViewSet for viewing own InstallmentPayment records.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = InstallmentPaymentSerializer

    def get_queryset(self):
        """
        Restrict queryset to the authenticated user's installment payments.
        """
        return InstallmentPayment.objects.filter(user=self.request.user)


@method_decorator(name='create', decorator=admin_create_immediate_payment_swagger)
@method_decorator(name='retrieve', decorator=admin_retrieve_immediate_payment_swagger)
@method_decorator(name='update', decorator=admin_update_immediate_payment_swagger)
@method_decorator(name='partial_update', decorator=admin_partial_update_immediate_payment_swagger)
@method_decorator(name='destroy', decorator=admin_destroy_immediate_payment_swagger)
@method_decorator(name='list', decorator=admin_list_immediate_payment_swagger)
class ImmediatePaymentAdminAPIView(ModelViewSet):
    """
    Admin-only API ViewSet for managing ImmediatePayment records.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = ImmediatePaymentSerializer
    queryset = ImmediatePayment.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username']


@method_decorator(name='retrieve', decorator=user_retrieve_immediate_payment_swagger)
@method_decorator(name='list', decorator=user_list_immediate_payment_swagger)
class ImmediatePaymentUserAPIView(ReadOnlyModelViewSet):
    """
    Authenticated user API ViewSet for viewing own ImmediatePayment records.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ImmediatePaymentSerializer

    def get_queryset(self):
        """
        Restrict queryset to the authenticated user's immediate payments.
        """
        return ImmediatePayment.objects.filter(user=self.request.user)