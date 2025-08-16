from rest_framework import serializers
from apps.package.models.insights import Category, FAQ, Comment





class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model.
    Converts Category instances to JSON and validates input data.
    """
    
    class Meta:
        model = Category
        fields = '__all__'  # Include all fields from the Category model


class FAQSerializer(serializers.ModelSerializer):
    """
    Serializer for FAQ model.
    Converts FAQ instances to JSON and validates input data.
    """
    
    class Meta:
        model = FAQ
        fields = '__all__'  # Include all fields from the FAQ model 
        
class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for Comment model.
    Converts Comment instances to JSON and validates input data.
    """
    
    class Meta:
        model = Comment
        fields = '__all__'  # Include all fields from the Comment model