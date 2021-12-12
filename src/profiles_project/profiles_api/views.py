from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Returns list of API Features"""
        an_apiview = [
            "Uses HTTP methods as functions- (GET, PUT, PATCH, POT, DELETE)",
            "Similar to traditional django view",
            "Gives most control over our logic" ,
            "Is mapped manually to URLs"
        ]
        return Response({'message': "Hello!", 'an_apiview': an_apiview})