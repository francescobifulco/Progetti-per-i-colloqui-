"""Progetto 3: "Semplice Gioco del Tris" (Tic-Tac-Toe)
Questo progetto ti permette di esplorare concetti più complessi come la 
programmazione a oggetti (OOP) e gli algoritmi di base. 
Creerai una versione del gioco del Tris che può essere giocata da due 
persone sulla stessa console.

Concetti chiave:
Programmazione a oggetti (OOP): Potresti creare una classe Game che 
gestisce lo stato del gioco (la scacchiera), 
e una classe Player che rappresenta i due giocatori.

Condizioni di vittoria: Dovrai scrivere una logica per verificare, 
dopo ogni mossa, se un giocatore ha vinto o se la partita è in parità. 
Questo richiede l'uso di cicli e condizioni per controllare righe, 
colonne e diagonali.

Gestione degli errori: Aggiungerai del codice per gestire le mosse non 
valide, come tentare di occupare una cella già piena."""

import random

class Player:
    def __init__(self, simbolo, nome_player):
        self.simbolo = simbolo
        self.nome_player = nome_player
        
    def scegli_simbolo(self):
        while True:
            scegli = input('scegli il simbolo: (x / o)').lower()
            if scegli =='x' or scegli =='o':
                self.simbolo = scegli
                print(f'il player {self.nome_player} hai scelto la {self.simbolo}')
                break
            else:
                print('Input non valido, riprova.')

class Game:
    def __init__(self, player1, player2):
        self.scacchiera = [' ']*9  # lista piatta 3x3
        self.player1 = player1
        self.player2 = player2
        self.turno_corrente = player1  # chi inizia
    
    def stampa_scacchiera(self):
        # Mostra la scacchiera in modo leggibile
        for i in range(3):
            riga = self.scacchiera[3*i:3*i+3]
            print('|'.join(riga))
            if i < 2:
                print('-'*5)
    
    def mossa_valida(self, posizione):
        # Controlla che la mossa sia in range e la casella sia libera
        return 0 <= posizione < 9 and self.scacchiera[posizione] == ' '
    
    def esegui_mossa(self, posizione):
        # Inserisce simbolo nella posizione, se valida
        if self.mossa_valida(posizione):
            self.scacchiera[posizione] = self.turno_corrente.simbolo
            return True
        else:
            return False
    
    def controlla_vittoria(self):
        s = self.scacchiera
        c = self.turno_corrente.simbolo
        vittorie = [
            [0,1,2], [3,4,5], [6,7,8],  # righe
            [0,3,6], [1,4,7], [2,5,8],  # colonne
            [0,4,8], [2,4,6]            # diagonali
        ]
        for trio in vittorie:
            if s[trio[0]] == s[trio[1]] == s[trio[2]] == c:
                return True
        return False
    
    def controlla_pareggio(self):
        return all(c != ' ' for c in self.scacchiera)
    
    def cambia_turno(self):
        if self.turno_corrente == self.player1:
            self.turno_corrente = self.player2
        else:
            self.turno_corrente = self.player1
    
    def gioca(self):
        print("Inizia il gioco!")
        while True:
            self.stampa_scacchiera()
            print(f"Tocca a {self.turno_corrente.nome_player} ({self.turno_corrente.simbolo})")
            
            try:
                pos = int(input("Inserisci una posizione da 0 a 8: "))
            except ValueError:
                print("Devi inserire un numero valido.")
                continue
            
            if not self.esegui_mossa(pos):
                print("Mossa non valida, riprova.")
                continue
            
            if self.controlla_vittoria():
                self.stampa_scacchiera()
                print(f"Complimenti {self.turno_corrente.nome_player}, hai vinto!")
                break
            
            if self.controlla_pareggio():
                self.stampa_scacchiera()
                print("Pareggio!")
                break
            
            self.cambia_turno()
    
p1 = Player("Alice", "X")
p2 = Player("Bob", "O")
game = Game(p1, p2)
game.gioca()
