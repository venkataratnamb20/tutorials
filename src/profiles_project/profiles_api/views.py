from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import serializers
from . import models
from . import permissions


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
class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message set"""
        a_viewset = [
            'user actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]
        return Response({'message': 'Hello', 'a_viewsets': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID"""
        return Response({"http_method": 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object by its ID"""
        return Response({"http_method": 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object by its ID"""
        return Response({"http_method": 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles deleting an object by its ID"""
        return Response({"http_method": 'DELETE'})



        
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles Creating and updating profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('firstname', 'lastname', 'email')

class LoginViewSet(viewsets.ViewSet):
    """Check mail and password and return authtoken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken to validate and create token"""
        return ObtainAuthToken().as_view()(request=request._request)
        # return ObtainAuthToken().post(request)