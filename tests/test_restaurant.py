"""Tests for the restaurant module."""

import pytest
from django.urls import reverse
from rest_framework import status
from restaurant.models import Restaurant


@pytest.mark.django_db
def test_list_restaurants(api_client):
    """Test listing restaurants."""
    url = reverse("restaurant-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_restaurant(api_client):
    """Test creating a restaurant."""
    url = reverse("restaurant-list")
    data = {"name": "New Restaurant", "is_available": True}
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Restaurant.objects.count() == 1
    restaurant = Restaurant.objects.first()
    assert restaurant.name == "New Restaurant"
    assert restaurant.is_available is True
