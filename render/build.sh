#!/bin/bash

# exit on error
set -o errexit

# Asegura que contamos con la ultima version de pip antes de instalar deps
pip install --upgrade pip

# Instala las dependencias del proyecto definidas en requirements.txt
pip install -r requirements.txt

# Recolecta archivos estaticos necesarios para el despliegue
python manage.py collectstatic --no-input

# Aplica migraciones pendientes a la base de datos antes de ejecutar
python manage.py migrate

# python build.py
