from rest_framework.pagination import PageNumberPagination


class DefaultPagination(PageNumberPagination):
    ordering = ['created_at', 'updated_at']
    page_size = 50
