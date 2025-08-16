from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from apps.core.models import StudentInformation,Teacher
from apps.core.serializers import StudentInformationSerializer,TeacherSerializer





class StudentInformationAdminAPIView(
    
    GenericAPIView,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    
):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = StudentInformationSerializer
    queryset = StudentInformation.objects.all()
    
    
class TeacherAdminAPIView(

    GenericAPIView,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    
):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    
    
class StudentInformationUserAPIView(
    
    GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    
):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StudentInformationSerializer
    
    def get_queryset(self):
        return StudentInformation.objects.filter(user=self.request.user)
    
class TeacherPublicAPIView(
    
    GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
):
    
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    