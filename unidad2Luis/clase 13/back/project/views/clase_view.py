from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from api.models.clase import Clase
from project.serializers.clase_serializer import ClaseSerializer
from django.http import Http404

class Clase_APIView(APIView):
    """
    API para listar y crear Clases
    """

    def get(self, request, format=None):
        queryset = Clase.objects.all()
        numero_clase = request.query_params.get('numero_clase')

        # Si el usuario envía ?numero_clase=2 se filtra
        if numero_clase:
            queryset = queryset.filter(numero_clase=numero_clase)

        serializer = ClaseSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ClaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Clase creada correctamente", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Clase_APIView_Detail(APIView):
    """
    API para obtener, actualizar o eliminar una Clase específica
    """

    def get_object(self, pk):
        try:
            return Clase.objects.get(pk=pk)
        except Clase.DoesNotExist:
            raise Http404("Clase no encontrada")

    def get(self, request, pk, format=None):
        clase = self.get_object(pk)
        serializer = ClaseSerializer(clase)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        clase = self.get_object(pk)
        serializer = ClaseSerializer(clase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Clase actualizada correctamente", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        clase = self.get_object(pk)
        clase.delete()
        return Response(
            {"message": "Clase eliminada correctamente"},
            status=status.HTTP_204_NO_CONTENT
        )
