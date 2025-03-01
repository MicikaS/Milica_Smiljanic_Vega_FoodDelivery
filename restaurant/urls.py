from django.urls import path
from .views import RestaurantViewSet, FoodViewSet

urlpatterns = [
    path(
        "",
        RestaurantViewSet.as_view({"get": "list", "post": "create"}),
        name="restaurant-list",
    ),
    path(
        "<int:pk>/",
        RestaurantViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="restaurant-detail",
    ),
    path(
        "menu/",
        FoodViewSet.as_view({"get": "list", "post": "create"}),
        name="food-list",
    ),
    path(
        "menu/<int:pk>/",
        FoodViewSet.as_view({"get": "retrieve", "delete": "destroy"}),
        name="food-detail",
    ),
]
