from django.urls import path
from .views import CreateUserView, UserListView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView


urlpatterns = [
    path("", CreateUserView.as_view(), name="register"),
    path("list/", UserListView.as_view(), name="user-list"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("password-reset/", PasswordResetView.as_view(), name="password_reset"),
    path(
        "password-reset-confirm/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]
