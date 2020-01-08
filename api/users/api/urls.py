from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ListUser, DetailUser, CreateUser, LogoutUser


urlpatterns = [
    path('register', CreateUser.as_view(), name="register-user"),
    path('login', TokenObtainPairView.as_view(), name="login-user"),
    path('logout', LogoutUser.as_view(), name="logout-user"),
    path('refresh', TokenRefreshView.as_view(), name="token-refresh"),
    path('', ListUser.as_view(), name="get-users"),
    path('<int:pk>', DetailUser.as_view(), name="get-user-by-id"),
]
