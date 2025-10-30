# cesar/urls.py

from django.urls import path
from .views import list_view, create_view, detail_view, edit_view, delete_view

app_name = "cesar"

# Define the URL patterns for the cesar app
urlpatterns = [
    # Pagina principal con el listado de frases
    path('', list_view, name="list"),
    # Formulario de creacion
    path('create/', create_view, name="create"),
    # Vista de detalle para una frase concreta
    path('<int:pk>/', detail_view, name="detail"),
    # Flujo de edicion y re-cifrado
    path('<int:pk>/edit/', edit_view, name="edit"),
    # Confirmacion y eliminacion definitiva
    path('<int:pk>/delete/', delete_view, name="delete"),   
]
