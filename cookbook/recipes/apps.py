from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RecipesConfig(AppConfig):
    name = "cookbook.recipes"
    verbose_name = _("Recipes")

    def ready(self):
        try:
            import cookbook.recipes.signals  # noqa F401
        except ImportError:
            pass