from django.db import models


# Create your models here.
# title
# year
# genre
# pagine
# email editore

class Books(models.Model):

    #CharField = campo testo con lunghezza massima 
    title = models.CharField(
        max_length=100
        verbose_name="Titolo"
        help_text="inserisci il titolo del libro")

    autore = models.CharField()
    
    
    year = models.PositiveIntegerField(max_length=100)
    genre = models.PositiveIntegerField()
    numero_pagine = models.DateField(null=True, blank=True)
    email_editore = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nome} {self.cognome}"