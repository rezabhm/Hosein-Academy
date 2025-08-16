from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.permissions import IsAdminUser, AllowAny,IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from apps.payment.models.payment import Transaction
from apps.payment.serializers.payment import PaymentSerializer






class TransactionAdminAPIView(
    
    GenericAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    
):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = PaymentSerializer
    queryset = Transaction.objects.all()
    
    
class TransactionUserAPIView(
    
    GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    
):
    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentSerializer
    
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
        
        
    