import regex as re
import hashlib

# Alfabeto base para el cifrado César / compatibilidad con caracteres españoles e ingleses
# Caracteres ASCII ingles
ASCII_ALPHABET = [chr(i) for i in range(32, 127)]
# Caracteres especificos del español
SPANISH_SUPPORT = list("áéíóúüñÁÉÍÓÚÜÑ¡¿°€£¥©®™•…“”‘’«»→←↑↓±×÷≈≠≤≥∞√πµ")
# Emojis porque si
EMOJIS = ["😀","😁","😂","🤣","😅","😊","😍","🤔","👍","👎","🔥","💡","✅","❌","❤️","🥳","😭","😡","🇨🇱","🚀"]

ALPHABET = ASCII_ALPHABET + SPANISH_SUPPORT + EMOJIS

# Funcion para dividir un texto en grafemas (evita separar caracteres compuestos)
def _split_grafema(text: str) -> list[str]:
    pattern = r'\X'
    return re.findall(pattern, text)

# Funcion para cifrar un texto usando el metodo Cesar
def cesar_encrypt(text: str, shift: int, alphabet: list[str] = ALPHABET) -> str:

    # Definir un index para cada caracter en el alfabeto
    position = {}
    for i, t in enumerate(alphabet):
        position[t] = i

    # Largo del alfabeto
    n = len(alphabet)

    # Lista vacia para almacenar el texto cifrado
    out = []

    # Recorrer cada grafema en el texto
    for g in _split_grafema(text):
        # Agregar el caracter cifrado o el mismo si no esta en el alfabeto
        out.append(alphabet[(position[g] + shift) % n] if g in position else g)
    
    # Retornar la lista unida como una cadena de texto
    return ''.join(out)
    
def cesar_decrypt(text: str, shift: int, alphabet: list[str] = ALPHABET) -> str:

    # Definir un index para cada caracter en el alfabeto
    position = {}
    for i, t in enumerate(alphabet):
        position[t] = i

    # Largo del alfabeto
    n = len(alphabet)

    # Lista vacia para almacenar el texto descifrado
    out = []

    # Recorrer cada grafema en el texto
    for g in _split_grafema(text):
        # Agregar el caracter descifrado o el mismo si no esta en el alfabeto
        out.append(alphabet[(position[g] - shift) % n] if g in position else g)
    
    # Retornar la lista unida como una cadena de texto
    return ''.join(out)

# Shift determinístico a partir de palabra mágica + salt
def derive_shift(password: str, shift_salt: str, alphabet: list[str] = ALPHABET) -> int:
    n = len(alphabet)
    h = hashlib.sha256((shift_salt + password).encode("utf-8")).digest()
    k = int.from_bytes(h, "big") % n
    return 1 if k == 0 else k