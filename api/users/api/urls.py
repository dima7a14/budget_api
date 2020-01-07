from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ListUser, DetailUser, CreateUser, LogoutUser


urlpatterns = [
    path('register', CreateUser.as_view(), name="Register user"),
    path('login', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('logout', LogoutUser.as_view(), name="Logout user"),
    path('refresh', TokenRefreshView.as_view(), name="token_refresh"),
    path('', ListUser.as_view(), name="Get users"),
    path('<int:pk>', DetailUser.as_view(), name="Get user by id"),
]
