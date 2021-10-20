from django.urls import path
from .views.client_views import clients_list_view, clients_detail_view
from .views.doc_type_views import doctypes_detail_view, doctypes_list_view
from .views.reserve_views import ReservsApiView, ReservsDetailApiView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Reserves Manage API",
      default_version='v1',
      description="Administrate the functionality of reserves for the CDA",
      terms_of_service="/policies/terms/",
      contact=openapi.Contact(email="contact@jepezdev.tech"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('clients/', clients_list_view, name='clients_list_view'),
    path('clients/<int:id>', clients_detail_view, name='clients_detail_view'),


    path('doctypes/', doctypes_list_view, name='doctypes_list_view'),
    path('doctypes/<int:id>', doctypes_detail_view, name='doctypes_detail_view'),

    path('reserves/', ReservsApiView.as_view(), name='reserves_list_view'),
    path('reserves/<int:id>', ReservsDetailApiView.as_view(), name='reserves_detail_view'),



   path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

