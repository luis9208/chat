from rest_framework import serializers
from chat.models import Profile, Mensajes
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensajes
        fields = ('content', 'user')