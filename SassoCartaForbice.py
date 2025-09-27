import random

class RoundGioco:
    mosse = ['Sasso', 'Carta', 'Forbice']
    def __init__(self,scelta_utente, punti):
        self.__scelta_utente = scelta_utente
        self.__scelta_computer = random.choice(RoundGioco.mosse)
        self.__punti = punti
    
    def determina_vincitore(self):
        print(f"Scelta utente: {self.__scelta_utente}")
        print(f"Scelta computer: {self.__scelta_computer}")

        if self.__scelta_utente == 'Sasso':
            if self.__scelta_computer == 'Forbice':
                print('hai vinto')
                self.__punti += 1
            elif self.__scelta_computer == 'Carta':
                print('hai perso')
                self.__punti -= 1
            elif self.__scelta_computer == 'Sasso':
                print('pareggio')
        
        elif self.__scelta_utente == 'Carta':
            if self.__scelta_computer == 'Forbice':
                print('hai perso')
                self.__punti -= 1
            elif self.__scelta_computer == 'Carta':
                print('pareggio')
            elif self.__scelta_computer == 'Sasso':
                print('hai vinto')
                self.__punti += 1
        
        elif self.__scelta_utente == 'Forbice':
            if self.__scelta_computer == 'Forbice':
                print('pareggio')
            elif self.__scelta_computer == 'Carta':
                print('hai vinto')
                self.__punti += 1
            elif self.__scelta_computer == 'Sasso':
                print('hai perso')
                self.__punti -= 1
        
        else:
            print("Scelta non valida. Devi scrivere 'Sasso', 'Carta' o 'Forbice'.")
        return self.__punti
    
    def visualizza_punti(self):
         return f'i tuoi punti sono {self.__punti}'

punti = 0

while True:
    scelta = input('vuoi gioare al gioco Sasso Carta Forbici (s/n): ').lower()
    if scelta == 's':
        mossa =input('inserisci la tua mossa: ').capitalize()
        if mossa not in RoundGioco.mosse:
            print("Mossa non valida. Riprova.")
            continue
        gioco = RoundGioco(mossa, punti)
        punti = gioco.determina_vincitore()
        print('-' * 20)
    elif scelta == 'n':
        print("Grazie per aver giocato!")
        print(f"Punteggio finale: {gioco.visualizza_punti()}")
        break
    else:
        print("Risposta non valida, inserisci 's' o 'n'.")