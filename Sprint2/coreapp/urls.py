from django.urls import path
from . import views

app_name = 'coreapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('cursos/', views.CursoListView.as_view(), name='cursos'),
    path('contacto/', views.ClienteCreateView.as_view(), name='contacto'),
    path('viewClientes/', views.ClienteListView.as_view(), name='viewClientes')
]
