from rest_framework.serializers import ModelSerializer
from .models import *
from django.contrib.auth.models import User, Group
from rest_framework import serializers
class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__' # for specific fields ['body','date']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','groups']
        
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url','name']

