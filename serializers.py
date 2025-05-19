
from rest_framework import serializers
from .models import Risk

class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risk
        fields = '__all__'
        read_only_fields = ['level', 'number', 'created_at']
