# cesar/urls.py

from django.urls import path
from .views import list_view

# Define the URL patterns for the cesar app
urlpatterns = [
    path("", list_view, name="list"),
]