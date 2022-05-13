from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework import permissions
from .views_auth import login, logout

class JokeViewSet(ModelViewSet):
    serializer_class = JokeSerializer

    def get_queryset(self):
        return Joke.objects.filter(creator=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class DogViewSet(ModelViewSet):
    serializer_class = DogSerializer

    def get_queryset(self):
        return Dog.objects.filter(creator=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return (permissions.AllowAny(),) # allow anonymous user access to create a new user (i.e. sign up)
        return (permissions.IsAdminUser(),) # block the rest, only for admins
