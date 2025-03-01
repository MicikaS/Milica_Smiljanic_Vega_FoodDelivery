"""Tests for the user module."""

import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_create_user(api_client):
    """Test creating a new user."""
    url = reverse("register")
    data = {
        "username": "testuser",
        "password": "testpassword123",
        "email": "testuser@example.com",
    }
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_user_list(api_client, create_user):
    """Test getting a list of users."""
    admin_user = create_user(username="admin", password="adminpass", is_staff=True)
    api_client.force_authenticate(user=admin_user)

    url = reverse("user-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0
