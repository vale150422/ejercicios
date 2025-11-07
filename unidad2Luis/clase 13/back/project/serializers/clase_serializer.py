from rest_framework import serializers
from api.models.clase import Clase


class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = ['id', 'tema', 'descripcion', 'numero_clase']
