# The Cesar Method

Dashboard web para cifrar y descifrar frases completas usando el **método de cifrado César**, desarrollado con **Django + Python**.

El proyecto fue creado como una aplicación web simple para practicar lógica de cifrado, estructura de proyecto Django, manejo de formularios, templates, archivos estáticos, variables de entorno y preparación básica para despliegue.

---

## Vista general

El cifrado César es una técnica clásica de sustitución en la que cada letra del mensaje se desplaza una cantidad fija de posiciones dentro del alfabeto.
Esta aplicación permite ingresar texto, definir un desplazamiento y obtener el resultado cifrado o descifrado desde una interfaz web.

---

## Características

* Cifrado de frases completas con desplazamiento configurable.
* Descifrado de texto previamente cifrado.
* Interfaz web construida con templates de Django.
* Separación entre configuración, aplicación principal, templates y archivos estáticos.
* Manejo de variables de entorno para configuración local.
* Preparación básica para despliegue en Render.
* Uso de entorno virtual y dependencias declaradas en `requirements.txt`.

---

## Stack utilizado

* **Python**
* **Django**
* **HTML**
* **CSS**
* **Shell script**
* **django-environ**
* **Render** para despliegue

---

## Estructura del proyecto

```txt
the-cesar-method/
├── cesar/              # Configuración principal del proyecto Django
├── core/               # Aplicación principal
├── render/             # Scripts/configuración de despliegue
├── static/
│   └── styles/         # Archivos CSS
├── templates/          # Templates HTML
├── manage.py
├── requirements.txt
└── README.md
```

---

## Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

* Python 3.11 o superior
* pip
* venv o virtualenv
* Git

---

## Instalación local

Clona el repositorio:

```bash
git clone https://github.com/codefusion-repo/the-cesar-method.git
cd the-cesar-method
```

Crea un entorno virtual:

```bash
python -m venv .venv
```

Activa el entorno virtual.

En Windows PowerShell:

```bash
.\.venv\Scripts\Activate.ps1
```

En Linux/macOS:

```bash
source .venv/bin/activate
```

Actualiza pip e instala las dependencias:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## Variables de entorno

El proyecto usa variables de entorno para manejar configuración sensible o dependiente del entorno.

Crea un archivo `.env` dentro de la carpeta `core/`:

```bash
core/.env
```

Contenido sugerido para desarrollo local:

```env
DEBUG=True
SECRET_KEY=coloca_aqui_una_clave_segura
ALLOWED_HOSTS=127.0.0.1,localhost
```

Puedes generar una `SECRET_KEY` segura ejecutando:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

> Importante: no subas archivos `.env` al repositorio. Usa un archivo `.env.example` si necesitas documentar variables sin exponer valores reales.

---

## Preparar la base de datos

Aplica las migraciones:

```bash
python manage.py migrate
```

Opcionalmente, crea un superusuario para acceder al panel de administración de Django:

```bash
python manage.py createsuperuser
```

---

## Ejecutar en desarrollo

Inicia el servidor local:

```bash
python manage.py runserver
```

Luego abre la aplicación en:

```txt
http://127.0.0.1:8000/
```

---

## Scripts útiles

El proyecto incluye un script de build para Render:

```txt
render/build.sh
```

Este script está pensado para preparar el despliegue instalando dependencias, recolectando archivos estáticos y aplicando migraciones según la configuración del entorno.

---

## Qué demuestra este proyecto

Este repositorio muestra práctica con:

* Estructura base de proyectos Django.
* Separación entre proyecto, aplicación, templates y archivos estáticos.
* Uso de variables de entorno.
* Manejo de dependencias con `requirements.txt`.
* Implementación de lógica de negocio simple en Python.
* Preparación básica para despliegue.
* Documentación de instalación y ejecución local.

---

## Estado del proyecto

Proyecto académico / demo técnica.

No busca ser una herramienta criptográfica segura para uso real. El cifrado César es un algoritmo clásico y educativo, útil para aprender conceptos de cifrado por sustitución, pero no debe usarse para proteger información sensible.

---

## Mejoras futuras

Algunas mejoras posibles:

* Agregar tests unitarios para la lógica de cifrado y descifrado.
* Mejorar validaciones de entrada.
* Agregar historial de operaciones.
* Incorporar soporte para caracteres especiales y distintos alfabetos.
* Agregar capturas de pantalla al README.
* Publicar una demo desplegada.
* Crear archivo `.env.example`.
* Configurar linting/formato automático.
