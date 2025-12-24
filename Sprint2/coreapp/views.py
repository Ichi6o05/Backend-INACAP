from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, edit
from .models import Curso, Contacto
from .forms import ContactoForm

def index(request):
    context = {
        'titulo': 'Bienvenidos a Nuestro Sitio',
        'descripcion': 'Descubre todos nuestros servicios y cursos'
    }
    return render(request, 'coreapp/index.html', context)

class CursoListView(ListView):
    model = Curso
    template_name = "coreapp/cursos.html"
    context_object_name = "cursos"

    def get_queryset(self):
        queryset = Curso.objects.all()
        query = self.request.GET.get("q")
        categoria = self.request.GET.get("categoria")

        if query:
            queryset = queryset.filter(titulo__icontains=query)
        if categoria:
            queryset = queryset.filter(categoria__iexact=categoria)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Nuestros Cursos"
        return context

class ClienteCreateView(edit.CreateView):
    model = Contacto
    form_class = ContactoForm
    template_name = "coreapp/contacto.html"
    success_url = reverse_lazy('coreapp:viewClientes')

    def get_initial(self):
        initial = super().get_initial()
        origen = self.request.GET.get("origen", "index")
        initial['origen'] = origen
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['origen'] = self.request.GET.get("origen", "index")
        context['cursos_disponibles'] = Curso.objects.all()
        return context

class ClienteListView(ListView):
    model = Contacto
    template_name = "coreapp/clientesList.html"
    context_object_name = "clientes"
    