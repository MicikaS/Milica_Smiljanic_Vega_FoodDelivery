from django.apps import AppConfig
from django.contrib.auth import get_user_model
import django


class FoodDeliveryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "food_delivery"

    def ready(self):
        """Automatically create a superuser if it doesn't exist"""
        if django.conf.settings.DEBUG:  # Only run in development mode
            User = get_user_model()
            if not User.objects.filter(is_superuser=True).exists():
                User.objects.create_superuser(
                    "admin", "admin@example.com", "adminpassword"
                )
                print("✅ Superuser created: admin/adminpassword")
