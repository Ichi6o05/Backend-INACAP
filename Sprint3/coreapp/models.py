from django.db import models
from django.utils import timezone

# Create your models here.
class Curso(models.Model):
    titulo = models.CharField(max_length=100, help_text="Ingrese titulo del curso")
    categoria = models.CharField(max_length=100, help_text="Ingrese la categoria del curso")
    descripcion = models.TextField(help_text="Ingrese una breve descripcion para el curso")
    duracion = models.CharField(max_length=50, help_text="Ingrese duracion del curso. Ej: 20 horas, 2 semanas...")
    precio = models.DecimalField(max_digits=6, decimal_places=2, help_text="Ingrese precio del curso. Ej: 39, 39.99")
    fecha_inicio = models.CharField(max_length=50, help_text="Ingrese fecha de inicio. Ej: 10 de enero")
    cupo = models.CharField(max_length=100, help_text="Ingrese cantidad de cupos. Ej: Max. 30 personas")
    imagen = models.ImageField(upload_to='imgCursos', null=True)

    def __str__(self):
        return f"{self.titulo} {self.categoria}"
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField(unique=False)
    telefono = models.CharField(max_length=20)
    mensaje = models.TextField(default="")
    origen = models.CharField(max_length=20, choices=[("index", "Index"), ("cursos", "Cursos")], default="index")
    curso = models.ForeignKey(
        Curso,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Seleccione el curso de interés"
    )
    fecha_envio = models.DateTimeField(default=timezone.now)
    cc_ami = models.BooleanField(default=False, help_text="Correo adicional (CC) opcional")
    
    def __str__(self):
        return f"{self.nombre} {self.email}"
    