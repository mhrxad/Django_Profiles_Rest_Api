from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from profiles_api_app import serializers


class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        return Response({'name': 'mehrzad'})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'message': 'Put request'})

    def patch(self, request, pk=None):
        return Response({'message': 'Patch request'})

    def delete(self, request, pk=None):
        return Response({'message': 'Delete request'})
