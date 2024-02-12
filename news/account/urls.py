from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path("signin", TokenObtainPairView.as_view(), name="create-token"),
    path("signup", views.UserCreateAPIView.as_view(), name="create-user"),
    path("refresh", TokenRefreshView.as_view(), name="refresh-token"),
    path("verify", TokenVerifyView.as_view(), name="verify-token"),
]