from django import forms

class CesarPhraseForm(forms.Form):
    clue = forms.CharField(label="Pista", max_length=120)
    text = forms.CharField(label="Texto a encriptar", widget=forms.Textarea)
    password = forms.CharField(label="Contraseña", max_length=200, widget=forms.PasswordInput)

class CesarDecryptForm(forms.Form):
    password = forms.CharField(label="Contraseña", max_length=200, widget=forms.PasswordInput)