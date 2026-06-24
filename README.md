<div align="center">

# The Cesar Method 🔐

### Dashboard web para cifrar y descifrar frases usando el método César

Proyecto desarrollado con **Django + Python** para practicar lógica de cifrado, estructura de aplicaciones web, manejo de formularios, templates, archivos estáticos y configuración por variables de entorno.

URL de pruebas: https://the-cesar-method.onrender.com/
</div>

---

## Vista general

**The Cesar Method** es una aplicación web simple que permite ingresar una frase, definir un desplazamiento y obtener el texto cifrado o descifrado utilizando el **cifrado César**.

El cifrado César es una técnica clásica de sustitución en la que cada letra del mensaje se desplaza una cantidad fija de posiciones dentro del alfabeto. En este proyecto se utiliza con fines educativos para practicar lógica, estructura de código y flujo básico de una aplicación Django.

---

## Funcionalidades

* Cifrado de frases completas.
* Descifrado de texto previamente cifrado.
* Desplazamiento configurable.
* Interfaz web construida con templates de Django.
* Separación entre configuración, aplicación principal, templates y archivos estáticos.
* Uso de variables de entorno para configuración local.
* Preparación básica para despliegue en Render.

---

## Stack utilizado

* **Python**
* **Django**
* **HTML**
* **CSS**
* **django-environ**
* **Render**

---

## Estructura del proyecto

```txt
the-cesar-method/
├── cesar/              # Aplicación principal
├── core/               # Configuración del proyecto Django
├── render/             # Scripts/configuración de despliegue
├── static/
│   └── styles/         # Archivos CSS
├── templates/          # Templates HTML
├── manage.py
├── requirements.txt
└── README.md
```

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

Instala las dependencias:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## Variables de entorno

Crea un archivo `.env` dentro de la carpeta `core/`:

```txt
core/.env
```

Contenido sugerido para desarrollo local:

```env
DEBUG=True
SECRET_KEY=coloca_aqui_una_clave_segura
ALLOWED_HOSTS=127.0.0.1,localhost
```

Puedes generar una `SECRET_KEY` segura con:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

> Importante: no subas archivos `.env` al repositorio. Para documentar variables sin exponer valores reales, usa un archivo `.env.example`.

---

## Ejecutar el proyecto

Aplica las migraciones:

```bash
python manage.py migrate
```

Inicia el servidor de desarrollo:

```bash
python manage.py runserver
```

Abre la aplicación en:

```txt
http://127.0.0.1:8000/
```

---

## Qué demuestra este proyecto

Este repositorio muestra práctica con:

* Estructura base de un proyecto Django.
* Uso de views, templates y archivos estáticos.
* Manejo de formularios y flujo de usuario.
* Implementación de lógica de negocio simple en Python.
* Configuración mediante variables de entorno.
* Preparación básica para despliegue.
* Documentación de instalación y ejecución local.

---

## Estado del proyecto

Proyecto académico / demo técnica.

No busca ser una herramienta criptográfica segura para uso real. El cifrado César es un algoritmo clásico y educativo, útil para aprender conceptos de cifrado por sustitución, pero no debe usarse para proteger información sensible.
