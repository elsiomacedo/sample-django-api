from rest_framework import serializers
from api.models import SampleModel


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleModel
        fields = '__all__'
