from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RecipeSerializer
from .models import Recipe


class RecipeViewSet(viewsets.ModelViewSet):
    """
    docstring
    """

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
