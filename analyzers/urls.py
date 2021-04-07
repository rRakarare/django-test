from django.urls import path,include
from rest_framework import routers
from .views import AnalyzerViewSet

router = routers.DefaultRouter()
router.register(r'analyzers', AnalyzerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]