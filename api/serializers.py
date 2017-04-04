"""
    Models serializers
"""
from rest_framework import serializers
from api.models import SampleModel


class SampleSerializer(serializers.ModelSerializer):
    """
        Sample model serializer
    """
    class Meta:
        """
            Default
        """
        model = SampleModel
        fields = '__all__'
