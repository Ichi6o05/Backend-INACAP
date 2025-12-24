from django.urls import path
from .views import ClienteListAPI
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('viewClientes/', ClienteListAPI.as_view(), name='apiViewClientes'),
    path('token/', obtain_auth_token, name='apiTokenAuth'),
]