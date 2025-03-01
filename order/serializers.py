from datetime import timedelta

from rest_framework import serializers
from .models import Order, Courier
from user.models import CustomUser
from restaurant.models import Restaurant, Food


class CourierSerializer(serializers.ModelSerializer):
    """Serializer for Courier model"""

    class Meta:
        model = Courier
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for Order model"""

    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    food = serializers.PrimaryKeyRelatedField(queryset=Food.objects.all(), many=True)
    courier = serializers.PrimaryKeyRelatedField(
        queryset=Courier.objects.all(), allow_null=True, required=False
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "restaurant",
            "food",
            "courier",
            "order_time",
            "estimated_delivery_time",
            "status",
        ]
        read_only_fields = ["order_time", "estimated_delivery_time"]

    def create(self, validated_data):
        """Custom create method to set estimated delivery time"""
        validated_data["estimated_delivery_time"] = validated_data[
            "order_time"
        ] + timedelta(minutes=15)
        return super().create(validated_data)
