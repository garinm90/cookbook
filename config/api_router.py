from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from cookbook.users.api.views import UserViewSet
from cookbook.recipes.api.views import IngredientViewSet, RecipeViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("recipes", RecipeViewSet)
router.register("ingredients", IngredientViewSet)


app_name = "api"
urlpatterns = router.urls
