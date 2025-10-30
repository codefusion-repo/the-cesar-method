# the-cesar-method

Dashboard para cifrar y descifrar frases completas con el método de cifrado César desarrollado con Django + Python.

## Requisitos previos

- Python 3.11 o superior recomendado.
- `pip` actualizado.
- `virtualenv` o `venv` para aislar dependencias.

## Instalación local paso a paso

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/<tu-usuario>/the-cesar-method.git
   cd the-cesar-method
   ```
   **Instala paquete de entornos virtuales 'virtualenv':**
   ```bash
   python -m pip install --user virtualenv
   ```
2. **Crea y activa un entorno virtual**
   ```bash
   python -m virtualenv env
   # Activar en Windows PowerShell
   .\.venv\Scripts\Activate.ps1
   # Activar en Linux/macOS
   source .venv/bin/activate
   # Activar en Git Bash
   source env/scripts/activate
   ```
3. **Actualiza `pip` e instala dependencias:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Variables de entorno necesarias

El proyecto usa `django-environ` y espera un archivo `core/.env`. Crea el archivo (si no existe) y define las variables mínimas:

Contenido sugerido de `core/.env`:

```env
# Activar modo depuración en local (usar False en producción)
DEBUG=True
# Clave secreta de Django (puedes generar una con: python -c "from django.core.management.utils import get_random_secret_key as k; print(k())")
SECRET_KEY=coloca_aqui_una_clave_segura
# Hosts permitidos separados por comas
ALLOWED_HOSTS=127.0.0.1,localhost
```

## Preparar y ejecutar la aplicación

1. **Aplica migraciones y prepara la base de datos:**
   ```bash
   python manage.py migrate
   ```
2. **(Opcional) Crea un superusuario para el panel admin:**
   ```bash
   python manage.py createsuperuser
   ```
3. **Inicia el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```
4. Abre tu navegador en `http://127.0.0.1:8000/` para usar la aplicación.

## Scripts útiles

- `render/build.sh`: script de despliegue que instala dependencias, recolecta estáticos y aplica migraciones automáticamente.
