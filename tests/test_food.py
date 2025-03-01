"""Tests for the food module."""

import pytest
from django.urls import reverse
from rest_framework import status
from restaurant.models import Food


@pytest.mark.django_db
def test_list_food(api_client):
    """Test listing food items."""
    url = reverse("food-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_food(api_client):
    """Test creating a food item."""
    url = reverse("food-list")
    data = {"name": "Pizza", "price": 9.99}
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Food.objects.count() == 1
    food = Food.objects.first()
    assert food.name == "Pizza"
    assert food.price == 9.99
