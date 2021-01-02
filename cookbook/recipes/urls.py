from django.urls import path
from .views import (
    RecipeCreateView,
    RecipeDetailView,
    RecipeListView,
    RecipeUpdateView,
    IngredientCreateView,
    IngredientDetailView,
    IngredientListView,
    IngredientUpdateView,
)


app_name = "recipes"
urlpatterns = [
    path("", RecipeListView.as_view(), name="recipes"),
    path("recipe/<int:pk>/", view=RecipeDetailView.as_view(), name="detail"),
    path("recipe/<int:pk>/update", view=RecipeUpdateView.as_view(), name="update"),
    path("recipe", view=RecipeCreateView.as_view(), name="create"),
    path("ingredients", IngredientListView.as_view(), name="ingredients"),
    path("ingredient/<int:pk>/", view=IngredientDetailView.as_view(), name="detail"),
    path(
        "ingredient/<int:pk>/update",
        view=IngredientUpdateView.as_view(),
        name="update",
    ),
    path("ingredient", view=IngredientCreateView.as_view(), name="create"),
]
