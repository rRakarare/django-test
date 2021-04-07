from rest_framework import viewsets
from .serializers import AnalyzerSerializer
from .models import Analyzer

class AnalyzerViewSet(viewsets.ModelViewSet):

    queryset = Analyzer.objects.all()
    serializer_class = AnalyzerSerializer
