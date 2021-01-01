from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from .serializers import RecipeSerializer, IngredientSerializer
from cookbook.recipes.models import Ingredient, Recipe


class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class IngredientViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer