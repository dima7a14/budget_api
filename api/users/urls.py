from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import UserList, UserDetail, UserUpdate

urlpatterns = [
    path("users", UserList.as_view(), name="Users list"),
    path("users/detail/", UserDetail.as_view(), name="User detail"),
    path("users/<int:pk>/", UserUpdate.as_view(), name="User update"),
]
