from django.urls import path
from apps.accounts import views


urlpatterns = [
    path('accounts/', views.UserApiView.as_view(), name='User Account'),
    path('accounts/login/', views.LoginApiView.as_view(), name='log in'),
]
