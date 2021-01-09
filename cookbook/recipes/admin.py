from django.contrib import admin
from .models import Ingredient, Recipe, IngredientQuantity


class IngredientQuantityInline(admin.TabularInline):
    model = IngredientQuantity
    extra = 3
@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientQuantityInline,)