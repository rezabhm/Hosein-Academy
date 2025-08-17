from rest_framework.routers import DefaultRouter

from apps.payment.api.v1.payment.view import TransactionUserAPIView, TransactionAdminAPIView
from apps.payment.api.v1.subscription.view import SubscriptionAdminAPIView, SubscriptionUserAPIView, \
    InstallmentPaymentUserAPIView, InstallmentPaymentAdminAPIView, ImmediatePaymentAdminAPIView, \
    ImmediatePaymentUserAPIView

router = DefaultRouter()

router.register('admin/subscription', SubscriptionAdminAPIView, basename='subscription-admin')
router.register('user/subscription', SubscriptionUserAPIView, basename='subscription-user')

router.register('admin/installment-payment', InstallmentPaymentAdminAPIView, basename='installment-payment-admin')
router.register('user/installment-payment', InstallmentPaymentUserAPIView, basename='installment-payment-user')

router.register('admin/immediate-payment', ImmediatePaymentAdminAPIView, basename='immediate-payment-admin')
router.register('user/immediate-payment', ImmediatePaymentUserAPIView, basename='immediate-payment-user')

router.register('admin/transaction', TransactionAdminAPIView, basename='transaction-admin')
router.register('user/transaction', TransactionUserAPIView, basename='transaction-user')

urlpatterns = router.urls
