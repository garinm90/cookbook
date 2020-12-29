from django.db import close_old_connections
from .models import Recipe, Ingredient, IngredientQuantity
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    """
    docstring
    """

    class Meta:
        model = Recipe
        fields = "__all__"
        depth = 2