from django.urls import path
from .views.client_views import clients_list_view, clients_detail_view
from .views.doc_type_views import doctypes_detail_view, doctypes_list_view
from .views.reserve_views import ReservsApiView, ReservsDetailApiView

urlpatterns = [
    path('clients/', clients_list_view, name='clients_list_view'),
    path('clients/<int:id>', clients_detail_view, name='clients_detail_view'),


    path('doctypes/', doctypes_list_view, name='doctypes_list_view'),
    path('doctypes/<int:id>', doctypes_detail_view, name='doctypes_detail_view'),

    path('reserves/', ReservsApiView.as_view(), name='reserves_list_view'),
    path('reserves/<int:id>', ReservsDetailApiView.as_view(), name='reserves_detail_view'),
    
]
