"""Progetto 2: Semplice Simulatore di Bank Account 💰
Questo progetto è un passo avanti e ti introdurrà all'ereditarietà, 
uno dei pilastri dell'OOP. 
L'obiettivo è simulare diversi tipi di conti bancari.

Concetti chiave:
Ereditarietà: Creerai una classe base ContoBancario con metodi comuni 
come deposito() e prelievo(). Successivamente, 
creerai classi figlie come ContoCorrente e ContoRisparmio che ereditano 
i metodi dalla classe base.
"""

class ContoBancario:
    def __init__(self, nome_cliente, mettere):
        self.__nome_cliente = nome_cliente
        self.__mettere = mettere
    
    def deposito(self):
        inserisci = float(input('inserisci il deposito da metere: '))
        if inserisci <= 0:
            print('inserimento non valito')
        else:
            self.__mettere += inserisci
            print(f'il/la signor ha depositato: {self.__mettere}')
    
    def prelievo(self):
        inserisci = float(input('inserisci il valore da preliero: '))
        if self.__mettere <= inserisci:
            print('il prelievo e maggiore')
        else:
            self.__mettere -= inserisci
            print(f'il/la signor ha prelevato: {inserisci}')
            print(f'il conto totale bancario e: {self.__mettere}')
        
    def __str__(self):
        return f"Cliente: {self.__nome_cliente} | Saldo: {self.__mettere}€"

dizionario_cliente = {}

while True:
    scelto = input('[A]ggiungi \n[D]eposito \n[P]relivo \n[L]ista clienti \n[E]sci \n').lower()
    if scelto == 'e':
        break
    elif scelto == 'a':
        nome = input('inserisci il tuo nome da cliente: ')
        saldo = float(input('mettere il deposito iniziale: '))
        conto = ContoBancario(nome, saldo)
        dizionario_cliente[nome] = conto
    elif scelto == 'd':
        nome = input('inserisci il nome del cliete per fare il deposito: ')
        if nome in dizionario_cliente:
            dizionario_cliente[nome].deposito()
        else: 
            print('cliente non trovato')
    elif scelto == 'p':
        nome = input('inserisci il nome del cliete per fare il prelievo: ')
        if nome in dizionario_cliente:
            dizionario_cliente[nome].prelievo()
        else: 
            print('cliente non trovato')
    elif scelto == 'l':
        if not dizionario_cliente:
            print("Nessun cliente registrato.")
        else:
            for conto in dizionario_cliente.values():
                print(conto)
    else:
        print('inserimento non valito')