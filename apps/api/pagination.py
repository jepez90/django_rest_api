from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'count'
    max_page_size = 500
    page_query_param = 'page'
