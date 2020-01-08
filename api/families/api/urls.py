from django.urls import path

from .views import ListFamily, DetailFamily

urlpatterns = [
    path('', ListFamily.as_view(), name="get-families"),
    path('<int:pk>', DetailFamily.as_view(), name="get-family-by-id"),
]
