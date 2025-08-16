from rest_framework import serializers
from apps.core.models import StudentInformation,Teacher



class StudentInformationSerializer(serializers.ModelSerializer):
    """
    Serializer for StudentInformation model.
    Converts StudentInformation instances to JSON and validates input data.
    """ 
    
    class Meta:
        model = StudentInformation
        fields = '__all__'  # Include all fields from the StudentInformation model  
        
        
class TeacherSerializer(serializers.ModelSerializer):
    """
    Serializer for Teacher model.
    Converts Teacher instances to JSON and validates input data.
    """
    
    class Meta:
        model = Teacher
        fields = '__all__'  # Include all fields from the Teacher model
        
