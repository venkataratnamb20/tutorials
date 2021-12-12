from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializer serializes a name field for testing"""
    firstname = serializers.CharField(max_length=50)
    