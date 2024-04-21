from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

# orm or object relational mapping maps python objects
# to the corresponding object that needs executed to make 
# a change to the database



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User #provided by django
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}} #noone should be able to read the password

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) #passing in the validated data from a dictionary
        return user
    

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}