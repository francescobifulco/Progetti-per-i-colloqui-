import random

class Carta:
    def __init__(self, seme, numero):
        self.__seme = seme
        self.__numero = numero
        
    # Getter per seme
    def get_seme(self):
        return self.__seme

    # Setter per seme
    def set_seme(self, nuovo_seme):
        self.__seme = nuovo_seme

    # Getter per numero
    def get_numero(self):
        return self.__numero

    # Setter per numero
    def set_numero(self, nuova_numero):
        self.__numero = nuova_numero
    
    def mostra(self):
        print(f'il valore della carta e {self.__numero} {self.__seme}')

class Mazzo: 
    def __init__(self):
        semi = ['coppe', 'denari', 'spade', 'dastoni']
        numeri = [1,2,3,4,5,6,7,8,9,10]
        # Creo tutte le carte del mazzo
        self.__carte = [Carta(seme, numero) for seme in semi for numero in numeri]
    
    def mischia(self):
        random.shuffle(self.__carte)
    
    def pesca_carta(self):
        if not self.__carte:
            return None
        else:
            carta = self.__carte.pop()
            return carta

class Giocatore:
    def __init__(self):
       self.__carte = []
       
    def ricevi_carta(self, carta):
        self.__carte.append(carta)

    
    def mostra_carte(self):
        for carta in self.__carte:
            carta.mostra()
    
mazzo = Mazzo()
mazzo.mischia()

giocatore = Giocatore()

carta_pescata = mazzo.pesca_carta()
if carta_pescata:
    giocatore.ricevi_carta(carta_pescata)

giocatore.mostra_carte()


