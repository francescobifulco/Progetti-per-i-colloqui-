"""Progetto 1: Sistema di Gestione di una Biblioteca 📚
Questo è un ottimo punto di partenza per l'OOP. 
L'obiettivo è creare classi che rappresentino gli oggetti del mondo 
reale, in questo caso, libri e membri della biblioteca.

Concetti chiave:
Classe e Oggetto: Creerai una classe Libro con attributi come titolo, 
autore, anno_pubblicazione, e disponibile. Ogni libro che creerai 
sarà un'istanza (oggetto) di questa classe.

Attributi e Metodi: La classe Libro avrà attributi per i dati e metodi 
come prendi_in_prestito() e restituisci() per cambiare lo stato di un 
libro (da disponibile a non disponibile e viceversa).

Encapsulamento: Utilizzerai l'incapsulamento per controllare l'accesso 
agli attributi. Per esempio, potresti rendere l'attributo disponibile 
modificabile solo tramite i metodi della classe, impedendo modifiche 
dirette e non autorizzate.

Crea anche una classe Membro per gestire i dati degli utenti 
(nome, ID, libri presi in prestito). Questo ti aiuterà a capire come gli 
oggetti possono interagire tra loro."""

class Libro:
    def __init__(self, titolo, autore, anno_pubblicazione, disponibile=True):
        self.__titolo = titolo
        self.__autore = autore
        self.__anno_pubblicazione = anno_pubblicazione
        self.__disponibile = disponibile
    
    def prendi_in_prestito(self):
            scegli_libro = input('scegli il libro da prendere: ')
            if self.__disponibile:
                self.__disponibile = False
                print(f"Hai preso in prestito: '{self.__titolo}'")
            else:
                print(f'il libro e gia in prestito')
    
    def restituisci(self):
            scegli_libro = input('scegli il libro da restituire: ')
            if not self.__disponibile:
                self.__disponibile = True
                print(f"Hai restituito il libro: '{self.__titolo}'")
            else:
                print(f'il libro non e stato prestato')

dizionazio_libro = {}

while True:
    scegli = input('[A]ggiunti \n[P]restito \n[R]estituisci \n[E]sci').lower()
    if scegli == 'e':
        break
    elif scegli == 'a':
        titolo = input('titolo del libro:').lower()
        autore = input('autore del libro:').lower()
        anno = input('anno di pubblicazione del libro:')
        disponibile = input('metti la disponibilita del libro')
        dizionazio_libro[Libro(titolo, autore, anno, disponibile)]