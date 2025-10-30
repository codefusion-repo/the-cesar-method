from django.db import models

# Modelo para almacenar frases cifradas con el método César
class Cesar_Phrase(models.Model):
    clue = models.CharField(max_length=120)
    encrypted = models.TextField()
    pass_hash = models.CharField(max_length=200)
    shift_salt = models.CharField(max_length=32)

    # Conserva la fecha de creacion para ordenar y auditar registros
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Representacion legible que muestra la pista asociada
        return f"Cesar Phrase (Clue: {self.clue})"
