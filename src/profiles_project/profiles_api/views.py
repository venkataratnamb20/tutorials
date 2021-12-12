from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns list of API Features"""
        an_apiview = [
            "Uses HTTP methods as functions- (GET, PUT, PATCH, POT, DELETE)",
            "Similar to traditional django view",
            "Gives most control over our logic" ,
            "Is mapped manually to URLs"
        ]
        return Response({'message': "Hello!", 'an_apiview': an_apiview})

    def post(self, request):
        """Create a Hello message with our name"""
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            firstname = serializer.data.get('firstname')
            message = 'Hello {0}'.format(firstname)
            return Response({'message': message, 'firstname': firstname}) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, pk=None):
        """Update object"""
        return Response({'method':'put'})

    def patch(self, request, pk=None):
        """Partial update"""
        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        """Delete object"""
        return Response({'method':'delete'})