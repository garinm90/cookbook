from django.db import models


class Recipe(models.Model):
    """
    docstring
    """

    recipe_name = models.CharField(max_length=100)

    pass


class RecipeIngredients(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    pass


class MeasurementUnit(models.Model):
    """
    docstring
    """

    VOLUME = "VL"
    MASS = "MS"
    OUNCES = "OZ"
    POUNDS = "LBS"
    GRAMS = "GR"
    FLUID_OUNCES = "FLOZ"
    MASS_OR_VOLUME_MEASUREMENT = [(VOLUME, "Volume"), (MASS, "Mass")]
    UNIT_OF_MEASUREMENT = [
        (OUNCES, "Ounces"),
        (POUNDS, "Pounds"),
        (GRAMS, "GR"),
        (FLUID_OUNCES, "Fluid Ounces"),
    ]

    recipe_ingredients_id = models.ForeignKey(
        RecipeIngredients, on_delete=models.CASCADE
    )
    mass_or_volume_measurement = models.CharField(
        max_length=2, choices=MASS_OR_VOLUME_MEASUREMENT, default=MASS
    )
    unit_of_measurement = models.CharField(
        max_length=4, choices=UNIT_OF_MEASUREMENT, default=GRAMS
    )

    def __str__(self) -> str:
        return f"Unit: {self.unit_of_measurement}"


class IngredientQuantity(models.Model):
    """
    docstring
    """

    recipe_ingredients_id = models.ForeignKey(
        RecipeIngredients, on_delete=models.CASCADE
    )
    ingredient_quantity = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self) -> str:
        return f"Quantity: {self.recipe_quantity}"


class Ingredient(models.Model):
    """
    docstring
    """

    recipe_ingredients_id = models.ForeignKey(
        RecipeIngredients, on_delete=models.CASCADE
    )
    ingredient_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.ingredient_name}"
