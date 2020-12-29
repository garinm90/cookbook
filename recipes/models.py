from django.db import models


class Recipe(models.Model):
    """
    docstring
    """

    recipe_name = models.CharField(max_length=100)
    ingredient = models.ManyToManyField(
        "Ingredient", related_name="recipes", through="IngredientQuantity"
    )
    print(ingredient)

    def __str__(self) -> str:
        return f"{self.recipe_name}"


# class RecipeIngredient(models.Model):
#     class Meta:
#         verbose_name = "Recipe Ingredient"
#         verbose_name_plural = "Recipe Ingredients"

#     recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     ingredient = models.ManyToManyField("Ingredient", blank=True)

#     def __str__(self) -> str:
#         return f"{self.recipe_id}"


class Ingredient(models.Model):
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
        (GRAMS, "Grams"),
        (FLUID_OUNCES, "Fluid Ounces"),
    ]

    mass_or_volume_measurement = models.CharField(
        max_length=2, choices=MASS_OR_VOLUME_MEASUREMENT, default=MASS
    )

    ingredient_name = models.CharField(max_length=100)
    unit_of_measurement = models.CharField(
        max_length=4, choices=UNIT_OF_MEASUREMENT, default=GRAMS
    )

    serving_size = models.IntegerField()
    fat_per_serving = models.PositiveIntegerField(default=0)
    carbohydrates_per_serving = models.PositiveIntegerField(default=0)
    protein_per_serving = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.ingredient_name}"


class IngredientQuantity(models.Model):
    """
    docstring
    """

    ingredient = models.ForeignKey(
        Ingredient, related_name="quantity", on_delete=models.RESTRICT
    )
    recipe = models.ForeignKey(
        Recipe, related_name="quantity", on_delete=models.RESTRICT
    )
    quantity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.recipe} uses {self.quantity} of {self.ingredient}"
