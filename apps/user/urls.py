from django.urls import path
from apps.user import views


urlpatterns = [
    path('users/', views.UserApiView.as_view(), name='register'),
    path('users/login/', views.LoginApiView.as_view(), name='log in '),
]
