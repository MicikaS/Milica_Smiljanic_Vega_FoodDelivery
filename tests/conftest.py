"""Fixtures for tests."""

import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from restaurant.models import Restaurant


@pytest.fixture
def api_client():
    """Return an instance of the APIClient."""
    return APIClient()


@pytest.fixture
def create_user():
    """Return a function to create a user."""

    def make_user(**kwargs):
        """Create a user with the given keyword arguments."""
        user = get_user_model()
        return user.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def restaurant(db):
    return Restaurant.objects.create(name="Test Restaurant", is_available=True)
