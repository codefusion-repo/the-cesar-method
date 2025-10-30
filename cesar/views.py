import secrets
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .models import Cesar_Phrase
from .forms import CesarPhraseCreateForm, CesarPhraseDecryptForm, CesarEditForm
from .utils import cesar_encrypt, cesar_decrypt, derive_shift

def list_view(request):
    items = Cesar_Phrase.objects.all().order_by('-created_at')
    return render(request, 'list.html', {'items': items})

def create_view(request):
    if request.method == 'POST':
        form = CesarPhraseCreateForm(request.POST)
        if form.is_valid():
            clue = form.cleaned_data['clue']
            text = form.cleaned_data['text']
            password = form.cleaned_data['password']
            
            shift_salt = secrets.token_hex(8)
            shift = derive_shift(password, shift_salt)

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
        form = CesarPhraseCreateForm()

    return render (request, 'create.html', {'form': form})
    
def detail_view(request, pk):
    cesar_phrase = get_object_or_404(Cesar_Phrase, pk=pk)
    plaintext = None
    shift = None
    form = CesarPhraseDecryptForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        password = form.cleaned_data['password']
        if check_password(password, cesar_phrase.pass_hash):
            shift = derive_shift(password, cesar_phrase.shift_salt)
            plaintext = cesar_decrypt(cesar_phrase.encrypted, shift)
        else:
            messages.error(request, 'Palabra mágica incorrecta. Inténtalo de nuevo.')

    return render (request, 'detail.html', {'form': form, 'obj': cesar_phrase, 'plaintext': plaintext, 'shift': shift})

def edit_view(request, pk):
    cesar_phrase = get_object_or_404(Cesar_Phrase, pk=pk)

    if request.method == 'POST':
        if 'verify' in request.POST:
            verify_form = CesarPhraseDecryptForm(request.POST)
            if verify_form.is_valid():
                password = verify_form.cleaned_data['password']
                if check_password(password, cesar_phrase.pass_hash):
                    shift = derive_shift(password, cesar_phrase.shift_salt)
                    text = cesar_decrypt(cesar_phrase.encrypted, shift)
                    edit_form = CesarEditForm(initial={
                        'clue': cesar_phrase.clue,
                        'text': text,
                        'password': password
                    })
                    return render (request, 'edit.html', {'verified': True, 'edit_form': edit_form, 'obj': cesar_phrase})
                else:
                    messages.error(request, 'Contraseña incorrecta. Inténtalo de nuevo.')

        if 'save' in request.POST:
            edit_form = CesarEditForm(request.POST)
            if edit_form.is_valid():
                clue = edit_form.cleaned_data['clue']
                text = edit_form.cleaned_data['text']
                new_password = edit_form.cleaned_data['new_password']
                password = edit_form.cleaned_data['password']
                if check_password(password, cesar_phrase.pass_hash):

                    cesar_phrase.clue = clue
                    if new_password:
                        shift_salt = secrets.token_hex(8)
                        shift = derive_shift(new_password, shift_salt)
                        encrypted_text = cesar_encrypt(text, shift)
                        pass_hash = make_password(new_password)

                        cesar_phrase.encrypted = encrypted_text
                        cesar_phrase.pass_hash = pass_hash
                        cesar_phrase.shift_salt = shift_salt
                    else:
                        shift = derive_shift(password, cesar_phrase.shift_salt)
                        encrypted_text = cesar_encrypt(text, shift)
                        cesar_phrase.encrypted = encrypted_text

                    cesar_phrase.save()
                    messages.success(request, 'Frase actualizada exitosamente.')
                    return redirect(reverse('cesar:detail', args=[cesar_phrase.id]))

    verify_form = CesarPhraseDecryptForm()
    return render (request, 'edit.html', {'verified': False, 'verify_form': verify_form, 'obj': cesar_phrase})

def delete_view(request, pk):
    cesar_phrase = get_object_or_404(Cesar_Phrase, pk=pk)
    if request.method == 'POST':
        cesar_phrase.delete()
        messages.success(request, 'Frase eliminada exitosamente.')
        return redirect(reverse('cesar:list'))
    return render (request, 'delete.html', {'obj': cesar_phrase})