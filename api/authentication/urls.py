from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

from .views import AuthViewSet

router = DefaultRouter()
router.register(r'', AuthViewSet, basename="auth")

urlpatterns = [
    *router.urls,
    path("login/", TokenObtainPairView.as_view(), name="login-user"),
    path("refresh/", TokenRefreshView.as_view(), name="token-refresh"),
]
