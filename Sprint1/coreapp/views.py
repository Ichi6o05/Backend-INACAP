from django.shortcuts import render

def index(request):
    """Vista para la página principal"""
    context = {
        'titulo': 'Bienvenidos a Nuestro Sitio',
        'descripcion': 'Descubre todos nuestros servicios y cursos'
    }
    return render(request, 'coreapp/index.html', context)


def cursos(request):
    """Vista para la página de cursos"""
    cursos = [
        {
            'titulo': 'Desarrollo Web Full Stack',
            'categoria': 'Tecnología',
            'descripcion': 'Aprende a crear aplicaciones web modernas',
            'duracion': '40 horas',
            'precio': 29,
            'fecha_inicio': '15 de enero',
            'cupo': 'Máx. 20 personas',
            'imagen': "https://picsum.photos/400/250?random=1"
        },
        {
            'titulo': 'Diseño Gráfico Creativo',
            'categoria': 'Arte y Diseño',
            'descripcion': 'Domina las herramientas del diseño gráfico profesional',
            'duracion': '30 horas',
            'precio': 24,
            'fecha_inicio': '20 de enero',
            'cupo': 'Máx. 15 personas',
            'imagen': "https://picsum.photos/400/250?random=2"
        },
        {
            'titulo': 'Marketing Digital Estratégico',
            'categoria': 'Negocios',
            'descripcion': 'Crea campañas efectivas en redes sociales',
            'duracion': '25 horas',
            'precio': 19,
            'fecha_inicio': '25 de enero',
            'cupo': 'Máx. 25 personas',
            'imagen': "https://picsum.photos/400/250?random=3"
        },
        {
            'titulo': 'Inglés para Negocios',
            'categoria': 'Idiomas',
            'descripcion': 'Mejora tu nivel de inglés enfocado en el ámbito empresarial y profesional.',
            'duracion': '50 horas',
            'precio': 19,
            'fecha_inicio': '1 de febrero',
            'cupo': 'Máx. 12 personas',
            'imagen': "https://picsum.photos/400/250?random=4"
        },
        {
            'titulo': 'Mindfulness y Gestión del Estrés',
            'categoria': 'Salud y Bienestar',
            'descripcion': 'Técnicas prácticas para mejorar tu bienestar emocional y reducir el estrés laboral.',
            'duracion': '20 horas',
            'precio': 17,
            'fecha_inicio': '10 de febrero',
            'cupo': 'Máx. 18 personas',
            'imagen': "https://picsum.photos/400/250?random=5"
        },
        {
            'titulo': 'Ciencia de Datos con Python',
            'categoria': 'Tecnología',
            'descripcion': 'Introducción al análisis de datos, machine learning y visualización con Python.',
            'duracion': '45 horas',
            'precio': 39,
            'fecha_inicio': '5 de febrero',
            'cupo': 'Máx. 16 personas',
            'imagen': "https://picsum.photos/400/250?random=6"
        },
    ]
    
    context = {
        'titulo': 'Nuestros Cursos',
        'cursos': cursos
    }
    return render(request, 'coreapp/cursos.html', context)


def contacto(request):
    origen = request.GET.get("origen", "index")
    context = {"origen": origen}
    return render(request, "coreapp/contacto.html", context)