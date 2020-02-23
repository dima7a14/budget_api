from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import UserList, UserDetail, UserUpdate

urlpatterns = [
    path("", UserList.as_view(), name="Users list"),
    path("detail/", UserDetail.as_view(), name="User detail"),
    path("<int:pk>/", UserUpdate.as_view(), name="User update"),
]
