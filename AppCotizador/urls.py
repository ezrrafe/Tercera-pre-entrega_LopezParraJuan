from django.urls import path
from AppCotizador.views import *


urlpatterns = [
    path('inicio/', inicio, name = "inicio"),
    path('crear_product/', crear_product, name = "crear_product"),
    path('crear_process/', crear_process, name = "crear_process"),
    path('crear_dimension/', crear_dimension, name = "crear_dimension"),
    path('crear_tooling/', crear_tooling, name = "crear_tooling"),
    path('buscar_product/', buscar_product, name = "crear_tooling")
]
