# cesar/urls.py

from django.urls import path
from .views import list_view, create_view, detail_view, edit_view, delete_view

app_name = "cesar"

# Define the URL patterns for the cesar app
urlpatterns = [
    path('', list_view, name="list"),
    path('create/', create_view, name="create"),
    path('<int:pk>/', detail_view, name="detail"),
    path('<int:pk>/edit/', edit_view, name="edit"),
    path('<int:pk>/delete/', delete_view, name="delete"),   
]