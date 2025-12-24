from django.contrib import admin
from .models import Curso, Contacto

# Register your models here.

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'descripcion', 'duracion', 'precio', 'fecha_inicio', 'cupo', 'imagen')
    list_filter = ("categoria",)

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'mensaje', 'origen', 'curso', 'fecha_envio')