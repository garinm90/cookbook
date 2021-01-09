from django.db import models
from django.db.models.fields import DecimalField, FloatField, PositiveIntegerField


class Recipe(models.Model):
    """
    
    """

    recipe_name = models.CharField(max_length=100)
    ingredient = models.ManyToManyField(
        "Ingredient", related_name="ingredients", through="IngredientQuantity"
    )
    number_of_servings = PositiveIntegerField()
    calories_per_meal = DecimalField(decimal_places=2, max_digits=6)
    fat_per_meal = DecimalField(decimal_places=2, max_digits=6)
    carbohydrates_per_meal = DecimalField(decimal_places=2, max_digits=6)
    protein_per_meal = DecimalField(decimal_places=2, max_digits=6)


    def __str__(self) -> str:
        return f"{self.recipe_name}"


class Ingredient(models.Model):
    """
    
    """

    VOLUME = "VL"
    FLUID_OUNCES = "FLOZ"
    TABLE_SPOON = "TBLSPN"
    CUPS = "CUPS"
    MASS = "MS"
    OUNCES = "OZ"
    POUNDS = "LBS"
    GRAMS = "GR"
    MASS_OR_VOLUME_MEASUREMENT = [(VOLUME, "Volume"), (MASS, "Mass")]
    UNIT_OF_MEASUREMENT = [
        (OUNCES, "Ounces"),
        (POUNDS, "Pounds"),
        (GRAMS, "Grams"),
        (FLUID_OUNCES, "Fluid Ounces"),
        (CUPS, "Cups"),
        (TABLE_SPOON, "Table Spoons")
    ]

    mass_or_volume_measurement = models.CharField(
        max_length=2, choices=MASS_OR_VOLUME_MEASUREMENT, default=MASS
    )

    ingredient_name = models.CharField(max_length=100)
    unit_of_measurement = models.CharField(
        max_length=10, choices=UNIT_OF_MEASUREMENT, default=GRAMS
    )

    units_per = models.DecimalField(decimal_places=2, max_digits=5)
    fat_per_serving = models.DecimalField(decimal_places=2, max_digits=5)
    carbohydrates_per_serving = models.DecimalField(decimal_places=2, max_digits=5)
    protein_per_serving = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self) -> str:
        return f"{self.ingredient_name}"


class IngredientQuantity(models.Model):
    """
    docstring
    """

    ingredient = models.ForeignKey(
        Ingredient, related_name="quantity", on_delete=models.PROTECT
    )
    recipe = models.ForeignKey(
        Recipe, related_name="quantity", on_delete=models.PROTECT
    )
    quantity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.recipe} uses {self.quantity} of {self.ingredient}"
