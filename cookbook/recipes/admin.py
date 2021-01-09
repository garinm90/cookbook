from django.contrib import admin
from django.db import models
from .models import Ingredient, Recipe, IngredientQuantity


class IngredientQuantityInline(admin.TabularInline):
    model = IngredientQuantity
    extra = 1
@admin.register(Ingredient, Recipe)
class CookbookAdmin(admin.ModelAdmin):
        inlines = (IngredientQuantityInline,)