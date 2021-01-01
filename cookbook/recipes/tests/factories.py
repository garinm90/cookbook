from factory import Faker, post_generation
from factory.django import DjangoModelFactory

from cookbook.recipes.models import Ingredient, Recipe


class RecipeFactory(DjangoModelFactory):
    recipe_name = "pizza"

    class Meta:
        model = Recipe