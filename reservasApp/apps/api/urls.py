from django.urls import path
from .views.client_views import clients_api_view, client_api_detail
from .views.doc_type_views import doc_types_api_view

urlpatterns = [
    path('clients/', clients_api_view, name='api_view_clients'),
    path('clients/<int:id>', client_api_detail, name='api_detail_clients'),


    path('doc_types/', doc_types_api_view, name='api_view_doc_types'),
]
