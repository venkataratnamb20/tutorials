from rest_framework import serializers

from . import models
class HelloSerializer(serializers.Serializer):
    """Serializer serializes a name field for testing"""
    firstname = serializers.CharField(max_length=50)
    
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for User profile object"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'firstname', 'lastname', 'password')

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile(
            email=validated_data['email'],
            firstname=validated_data['firstname'],
            lastname=validated_data['lastname']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
