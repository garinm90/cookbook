from django.contrib import admin
from .models import (
    Ingredient,
    IngredientQuantity,
    # IngredientQuantity,
    # MeasurementUnit,
    Recipe,
)


@admin.register(Ingredient, Recipe, IngredientQuantity)
class RecipeAdmin(admin.ModelAdmin):
    pass