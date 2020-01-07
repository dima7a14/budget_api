from rest_framework.pagination import CursorPagination


class DefaultPagination(CursorPagination):
    ordering = ['created_at', 'updated_at']
    page_size = 50
