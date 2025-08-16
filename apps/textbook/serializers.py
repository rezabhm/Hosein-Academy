from rest_framework import serializers

from apps.textbook.models import TextBook


class TextBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextBook
        fields = '__all__'
