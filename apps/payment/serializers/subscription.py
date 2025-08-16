from rest_framework import serializers

from apps.payment.models.subscription import Subscription, InstallmentPayment, ImmediatePayment


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class InstallmentPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstallmentPayment
        fields = '__all__'


class ImmediatePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImmediatePayment
        fields = '__all__'
