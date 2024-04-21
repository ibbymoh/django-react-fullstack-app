from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here.

class NotesListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer): 
        if serializer.is_valid(): #checks if the serializer object is valid and all of the fields passed in match what was specified in the model
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
class CreateUserReview(generics.CreateAPIView):
    queryset = User.objects.all() #List of objects we look at when creating a new one to make sure we dont create a user that already exists
    serializer_class = UserSerializer #data we need to accept to create a new user
    permission_classes = [AllowAny] #specified who can actually call this
