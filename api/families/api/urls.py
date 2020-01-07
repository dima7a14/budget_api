from django.urls import path

from .views import ListFamily, DetailFamily

urlpatterns = [
    path('', ListFamily.as_view(), name="Get families"),
    path('<int:pk>', DetailFamily.as_view(), name="Get family by id"),
]
