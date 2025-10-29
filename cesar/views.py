import secrets
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .models import Cesar_Phrase
from .forms import CesarPhraseForm, CesarDecryptForm
from .utils import cesar_encrypt, cesar_decrypt, derive_shift

def list_view(request):
    items = Cesar_Phrase.objects.all().order_by('-created_at')
    return render(request, 'templates/list.html', {'items': items})

def create_view(request):
    if request.method == 'POST':
        form = CesarPhraseForm(request.POST)
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
            form = CesarPhraseForm()

        return render (request, 'templates/create.html', {'form': form})
    
def detail_view(request, pk):
    cesar_phrase = get_object_or_404(Cesar_Phrase, pk=pk)
    decrypted_text = None

    form = CesarDecryptForm(request.POST or None)

    return