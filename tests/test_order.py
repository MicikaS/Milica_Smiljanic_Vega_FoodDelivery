# test_order.py
import pytest
from django.urls import reverse
from rest_framework import status

from order.models import Order


@pytest.mark.django_db
def test_list_orders(api_client, create_user):
    """Test listing orders."""
    user = create_user(username="testuser", password="testpass")
    api_client.force_authenticate(user=user)
    url = reverse("order-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_order(api_client, create_user, restaurant):
    """Test creating an order."""
    user = create_user(username="testuser", password="testpass")
    api_client.force_authenticate(user=user)
    url = reverse("order-list")
    data = {"delivery_location": "123 Test St", "items": "Pizza"}
    response = api_client.post(url, data, format="json")
    print(response.data)

    assert response.status_code == status.HTTP_201_CREATED
    assert Order.objects.count() == 1
    order = Order.objects.first()
    assert order.restaurant == restaurant
