from django.contrib import admin
from .models import (
    Ingredient,
    IngredientQuantity,
    MeasurementUnit,
    Recipe,
    RecipeIngredients,
)


@admin.register(
    Ingredient, IngredientQuantity, MeasurementUnit, Recipe, RecipeIngredients
)
class RecipeAdmin(admin.ModelAdmin):
    pass