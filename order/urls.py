from django.urls import path
from .views import OrderViewSet, CourierViewSet

urlpatterns = [
    path(
        "", OrderViewSet.as_view({"get": "list", "post": "create"}), name="order-list"
    ),
    path("<int:pk>/", OrderViewSet.as_view({"get": "retrieve"}), name="order-detail"),
    path("courier/", CourierViewSet.as_view({"get": "list"}), name="courier-list"),
    path(
        "courier/<int:pk>/",
        CourierViewSet.as_view({"get": "retrieve"}),
        name="courier-detail",
    ),
]
