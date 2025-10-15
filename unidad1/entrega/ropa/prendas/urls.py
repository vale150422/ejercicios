from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RopaViewSet, inicio

router = DefaultRouter()
router.register(r'prendas', RopaViewSet, basename='prendas')

urlpatterns = [
    path('', inicio, name='inicio'),
    path('', include(router.urls)),
]
