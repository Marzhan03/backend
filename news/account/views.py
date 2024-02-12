from django.shortcuts import render

from . import serializers, models
from rest_framework import generics

# Create your views here.

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.CustomUserSerializer
