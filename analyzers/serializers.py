from .models import Analyzer
from rest_framework import serializers

class AnalyzerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analyzer
        fields = ['name']