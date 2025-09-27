import random

class Giocatore:
    def __init__(self, nome, soldi):
        self.nome = nome
        self.soldi = soldi
    
    def stampa(self):
        print(f'Il giocatore {self.nome} ha € {self.soldi} nel deposito.')
        
    def aggiorna_soldi(self, importo):
        self.soldi += importo

    def get_soldi(self):
        return self.soldi
    
    
class Game:
    def __init__(self, giocatore, facce=6):
        self.facce = facce
        self.giocatore  = giocatore 
            
    def lancia(self, scelta_utente):
        print(f"Il giocatore {self.giocatore.nome}: {scelta_utente}")
        lancio = random.randint(1, self.facce)
        if scelta_utente == lancio:
            self.giocatore.aggiorna_soldi(100)
            print(f'hai vinto € 100 ora il tuo deposito vale € {self.giocatore.get_soldi()}')
        else:
            self.giocatore.aggiorna_soldi(-100)
            print(f'hai perso € 100 ora il tuo deposito vale € {self.giocatore.get_soldi()}')
            print(f'il numero uscito e: {lancio}')
        if self.giocatore.get_soldi() <= 0:
            print("Hai esaurito il tuo deposito. Fine del gioco.")
            return False
        return True
        
        
while True:
    scelta = input('vuoi giocare al gioco dei dati (s/n): ').lower()
    if scelta == 's':
        nome = input('inserire il tuo nome: ')
        try:
            soldi = int(input('inserire quanti soldi vuoi puntare: '))
        except ValueError:
            print("Importo non valido. Deve essere un numero intero.")
            continue
        
        giocatore = Giocatore(nome, soldi)
        gioco = Game(giocatore)
        giocatore.stampa()
        while giocatore.get_soldi() > 0:
            try:
                lanciare = int(input('scegli un numero tra (1 a 6): '))
                if lanciare < 1 or lanciare > 6:
                    print("Numero non valido. Devi scegliere tra 1 e 6.")
            except ValueError:
                print("Input non valido. Inserisci un numero.")
                continue
            gioco.lancia(lanciare)
            vuoi = input("Vuoi continuare a giocare? (s/n): ").lower()
            if vuoi != 's':
                print("Hai scelto di terminare il gioco. Grazie per aver giocato!")
                break
            elif scelta == 'n':
                print("Alla prossima!")
                break
    else:
        print("Risposta non valida, inserisci 's' o 'n'.")