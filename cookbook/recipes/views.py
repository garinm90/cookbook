from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView, ListView, CreateView

from .models import Ingredient, Recipe


class RecipeDetailView(DetailView):
    model = Recipe


class RecipeListView(ListView):
    model = Recipe


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = "__all__"


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe


class IngredientDetailView(DetailView):
    model = Ingredient


class IngredientListView(ListView):
    model = Ingredient


class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    fields = "__all__"


class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredient