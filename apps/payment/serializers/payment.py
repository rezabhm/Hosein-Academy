from rest_framework import serializers

from apps.payment.models.payment import Transaction


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'
