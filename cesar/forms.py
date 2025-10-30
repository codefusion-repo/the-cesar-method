from django import forms

# Formulario principal para crear frases cifradas con pista y contrasena
class CesarPhraseCreateForm(forms.Form):
    clue = forms.CharField(label="Pista", max_length=120)
    text = forms.CharField(label="Texto a encriptar", widget=forms.Textarea)
    password = forms.CharField(label="Contraseña", max_length=200, widget=forms.PasswordInput)

# Formulario sencillo para validar la palabra magica sin exponerla
class CesarPhraseDecryptForm(forms.Form):
    password = forms.CharField(label="Contraseña", max_length=200, widget=forms.PasswordInput)

# Formulario que permite editar pistas, texto y cambiar la contrasena si se desea
class CesarEditForm(forms.Form):
    clue = forms.CharField(label="Pista", max_length=120)
    text = forms.CharField(label="Nuevo texto a encriptar", widget=forms.Textarea)
    new_password = forms.CharField(label="Nueva contraseña", max_length=200, widget=forms.PasswordInput, required=False)
    password = forms.CharField(label="Contraseña actual", max_length=200, widget=forms.PasswordInput, required=True)
