from django import forms

class CesarPhraseCreateForm(forms.Form):
    clue = forms.CharField(label="Pista", max_length=120)
    text = forms.CharField(label="Texto a encriptar", widget=forms.Textarea)
    password = forms.CharField(label="Contraseña", max_length=200, widget=forms.PasswordInput)

class CesarPhraseDecryptForm(forms.Form):
    password = forms.CharField(label="Contraseña", max_length=200, widget=forms.PasswordInput)

class CesarEditForm(forms.Form):
    clue = forms.CharField(label="Pista", max_length=120)
    text = forms.CharField(label="Nuevo texto a encriptar", widget=forms.Textarea)
    new_password = forms.CharField(label="Nueva contraseña", max_length=200, widget=forms.PasswordInput, required=False)
    password = forms.CharField(label="Contraseña actual", max_length=200, widget=forms.PasswordInput, required=True)