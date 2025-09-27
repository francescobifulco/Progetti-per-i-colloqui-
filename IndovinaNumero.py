"""Progetto 1: "Indovina il Numero" (OOP Edition) 🧠
Questo progetto è un ottimo punto di partenza per familiarizzare con le 
classi, gli oggetti, gli attributi e i metodi in un contesto di gioco. 
L'obiettivo è trasformare il classico gioco "Indovina il Numero" 
in un'applicazione orientata agli oggetti.

Concetti chiave di OOP:
Classe Game: Sarà il cuore del tuo gioco. Gestirà la logica principale.

Attributi: numero_segreto, tentativi_rimanenti, limite_tentativi.

Metodi:

__init__: Inizializza il numero segreto casuale e i tentativi.

start(): Avvia il ciclo di gioco, 
gestisce l'input dell'utente e controlla le condizioni di 
vittoria/sconfitta.

check_guess(guess): Controlla se il numero indovinato è corretto, 
troppo alto o troppo basso, e aggiorna i tentativi.

is_game_over(): Determina se il gioco è finito 
(numero indovinato o tentativi esauriti).

Scopo del Progetto:
Imparare a incapsulare la logica di gioco all'interno di una singola 
classe, rendendo il codice più organizzato e riutilizzabile. 
Capirai come gli attributi mantengono lo stato del gioco e come i metodi 
manipolano questo stato.
"""

import random

class Game:
    def __init__(self, massimo=100, limite_tentativi=3):
        self.__numero_segreto = random.randint(0, massimo)
        self.__limite_tentativi = limite_tentativi
        self.__tentativi_rimanenti = limite_tentativi
        self.__game_over = False

    def start(self):
        print(f"""Benvenuto! Hai {self.__limite_tentativi} tentativi per
              indovinare il numero segreto (tra 0 e 100). Premi invio per iniziare.""")
        input()
        self.gioca()

    def gioca(self):
        while not self.is_game_over():
            try:
                guess = int(input("Inserisci il tuo numero: "))
            except ValueError:
                print("Errore: devi inserire un numero intero valido.")
                continue

            self.check_guess(guess)

        if not self.__game_over:
            print(f"Hai perso! Il numero segreto era {self.__numero_segreto}.")

    def check_guess(self, guess):
        if guess == self.__numero_segreto:
            print(f"Hai indovinato il numero segreto: {self.__numero_segreto}!")
            print(f"Hai usato {self.__limite_tentativi - self.__tentativi_rimanenti + 1} tentativi.")
            self.__game_over = True
        elif guess < self.__numero_segreto:
            self.__tentativi_rimanenti -= 1
            print("Il numero segreto è più alto.")
            self.print_tentativi()
        else:
            self.__tentativi_rimanenti -= 1
            print("Il numero segreto è più basso.")
            self.print_tentativi()

    def print_tentativi(self):
        if self.__tentativi_rimanenti > 0:
            print(f"Tentativi rimasti: {self.__tentativi_rimanenti}\n")

    def is_game_over(self):
        return self.__game_over or self.__tentativi_rimanenti == 0

# --- Ciclo principale ---
while True:
    vuoi = input('Vuoi giocare a "Indovina il numero"? (s/n): ').strip().lower()
    if vuoi == 'n':
        print("Grazie per aver giocato!")
        break
    elif vuoi == 's':
        gioco = Game()
        gioco.start()
    else:
        print("Risposta non valida. Scrivi 's' per sì o 'n' per no.")
