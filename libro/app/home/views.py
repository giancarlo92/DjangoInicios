from django.shortcuts import render

from django.views.generic import (
    TemplateView,
    ListView
)

class IndexView(TemplateView):
    template_name = "home/index.html"

class ListaLibros(ListView):
    template_name = "home/lista.html"
    queryset = ["El quijote de la mancha", "Codigo Limpio", "La sombra del viento", "La casa Matusita"]
    context_object_name = "libros"