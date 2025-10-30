import secrets
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .models import Cesar_Phrase
# Formularios utilizados a lo largo del flujo de creacion, consulta y edicion
from .forms import CesarPhraseCreateForm, CesarPhraseDecryptForm, CesarEditForm
# Funciones auxiliares que encapsulan la logica del cifrado Cesar
from .utils import cesar_encrypt, cesar_decrypt, derive_shift

# Muestra el listado de frases ordenadas por fecha de creacion descendente
def list_view(request):
    # Recupera todas las frases usando el orden mas reciente primero
    items = Cesar_Phrase.objects.all().order_by('-created_at')
    return render(request, 'list.html', {'items': items})

# Gestiona el formulario para registrar y cifrar nuevas frases
def create_view(request):
    # Gestiona la captura de datos y el cifrado inicial de una frase
    if request.method == 'POST':
        form = CesarPhraseCreateForm(request.POST)
        if form.is_valid():
            # Extraer la pista, el texto y la contrasena ingresados
            clue = form.cleaned_data['clue']
            text = form.cleaned_data['text']
            password = form.cleaned_data['password']
            
            # Generar un salt aleatorio que evita reutilizar desplazamientos
            shift_salt = secrets.token_hex(8)
            shift = derive_shift(password, shift_salt)

            # Cifrar el texto y almacenar la contrasena como hash seguro
            encrypted_text = cesar_encrypt(text, shift)
            pass_hash = make_password(password) 

            cesar_phrase = Cesar_Phrase.objects.create(
                clue=clue,
                encrypted=encrypted_text,
                pass_hash=pass_hash,
                shift_salt=shift_salt,
            )

            messages.success(request, 'Frase cifrada creada exitosamente.')
            return redirect(reverse('cesar:detail', args=[cesar_phrase.id]))
    else:
        # Para solicitudes GET se muestra un formulario vacio
        form = CesarPhraseCreateForm()

    # Entregar el formulario actual (con errores o limpio segun corresponda)
    return render (request, 'create.html', {'form': form})
# Proporciona visualizacion detallada y permite descifrar una frase especifica
def detail_view(request, pk):
    # Permite consultar la informacion cifrada y realizar el descifrado validando la contrasena
    cesar_phrase = get_object_or_404(Cesar_Phrase, pk=pk)
    plaintext = None
    shift = None
    form = CesarPhraseDecryptForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # Recuperar la palabra magica enviada en el formulario
        password = form.cleaned_data['password']
        if check_password(password, cesar_phrase.pass_hash):
            # Derivar el desplazamiento asociado y descifrar el contenido
            shift = derive_shift(password, cesar_phrase.shift_salt)
            plaintext = cesar_decrypt(cesar_phrase.encrypted, shift)
        else:
            messages.error(request, 'Palabra mágica incorrecta. Inténtalo de nuevo.')

    return render (request, 'detail.html', {'form': form, 'obj': cesar_phrase, 'plaintext': plaintext, 'shift': shift})

# Permite editar la pista, el contenido y opcionalmente cambiar la contrasena
def edit_view(request, pk):
    cesar_phrase = get_object_or_404(Cesar_Phrase, pk=pk)

    if request.method == 'POST':
        # Primer paso: verificar la contrasena actual antes de permitir cambios
        if 'verify' in request.POST:
            verify_form = CesarPhraseDecryptForm(request.POST)
            if verify_form.is_valid():
                password = verify_form.cleaned_data['password']
                if check_password(password, cesar_phrase.pass_hash):
                    shift = derive_shift(password, cesar_phrase.shift_salt)
                    text = cesar_decrypt(cesar_phrase.encrypted, shift)
                    # Precarga el formulario de edicion con el texto plano original
                    edit_form = CesarEditForm(initial={
                        'clue': cesar_phrase.clue,
                        'text': text,
                        'password': password
                    })
                    return render (request, 'edit.html', {'verified': True, 'edit_form': edit_form, 'obj': cesar_phrase})
                else:
                    messages.error(request, 'Contraseña incorrecta. Inténtalo de nuevo.')

        if 'save' in request.POST:
            # Una vez verificada la contrasena se procesa la actualizacion
            edit_form = CesarEditForm(request.POST)
            if edit_form.is_valid():
                clue = edit_form.cleaned_data['clue']
                text = edit_form.cleaned_data['text']
                new_password = edit_form.cleaned_data['new_password']
                password = edit_form.cleaned_data['password']
                # Verifica nuevamente la credencial para prevenir cambios no autorizados
                if check_password(password, cesar_phrase.pass_hash):

                    cesar_phrase.clue = clue
                    if new_password:
                        # Contrasena nueva implica nuevo salt y recifrado completo
                        shift_salt = secrets.token_hex(8)
                        shift = derive_shift(new_password, shift_salt)
                        encrypted_text = cesar_encrypt(text, shift)
                        pass_hash = make_password(new_password)

                        cesar_phrase.encrypted = encrypted_text
                        cesar_phrase.pass_hash = pass_hash
                        cesar_phrase.shift_salt = shift_salt
                    else:
                        # Si no cambia la contrasena se reutiliza el salt existente
                        shift = derive_shift(password, cesar_phrase.shift_salt)
                        encrypted_text = cesar_encrypt(text, shift)
                        cesar_phrase.encrypted = encrypted_text
                    # Guardar los cambios en la base y notificar al usuario
                    cesar_phrase.save()
                    messages.success(request, 'Frase actualizada exitosamente.')
                    return redirect(reverse('cesar:detail', args=[cesar_phrase.id]))

    verify_form = CesarPhraseDecryptForm()
    # Renderiza el formulario inicial cuando aun no se valida la contrasena
    return render (request, 'edit.html', {'verified': False, 'verify_form': verify_form, 'obj': cesar_phrase})

# Permite eliminar frases una vez confirmada la accion desde el formulario
def delete_view(request, pk):
    cesar_phrase = get_object_or_404(Cesar_Phrase, pk=pk)
    if request.method == 'POST':
        # Solo se borra despues de confirmar con peticion POST
        cesar_phrase.delete()
        messages.success(request, 'Frase eliminada exitosamente.')
        return redirect(reverse('cesar:list'))
    # Mostrar pagina de confirmacion cuando no se ha enviado el formulario
    return render (request, 'delete.html', {'obj': cesar_phrase})
