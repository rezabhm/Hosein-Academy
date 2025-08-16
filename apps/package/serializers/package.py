from rest_framework import serializers
from apps.package.models.package import Course,Season,Lesson





class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer for Course model.
    Converts Course instances to JSON and validates input data.
    """
    
    class Meta:
        model = Course
        fields = '__all__'  # Include all fields from the Course model

        
class SeasonSerializer(serializers.ModelSerializer):
    """
    Serializer for Season model.
    Converts Season instances to JSON and validates input data.
    """
    class Meta:
        model = Season
        fields = '__all__'  # Include all fields from the Season model
        

class LessonSerializer(serializers.ModelSerializer):
    """
    Serializer for Lesson model.
    Converts Lesson instances to JSON and validates input data.
    """
    class Meta:
        model = Lesson
        fields = '__all__'  # Include all fields from the Lesson model
        
