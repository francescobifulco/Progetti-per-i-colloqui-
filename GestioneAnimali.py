class Animale:
    def __init__(self, nome, eta):
        self.__nome = nome
        self.__eta = eta
    
    # Getter per nome
    def get_nome(self):
        return self.__nome

    # Setter per nome
    def set_nome(self, nuovo_nome):
        self.__nome = nuovo_nome

    # Getter per eta
    def get_eta(self):
        return self.__eta

    # Setter per eta
    def set_eta(self, nuova_eta):
        self.__eta = nuova_eta
    
    def emetti_suono(self):
        print('animale fa')
    
    def presentati(self):
        print(f'animale di nome {self.__nome} e la sua eta e {self.__eta}')

class Cane(Animale):
    def __init__(self, nome, eta, razza):
        super().__init__(nome, eta)
        self.__razza = razza
    
    def presentati(self):
        print(f'''Il cane di nome {self.get_nome()} e la sua eta e {self.get_eta()}
              e la sua razza e {self.__razza}''')
        
    def emetti_suono(self):
        print('Il cane fa Bau!')

class Getto(Animale):
    def __init__(self, nome, eta, colore_pelliccia):
        super().__init__(nome, eta)
        self.__colore_pelliccia = colore_pelliccia
    
    def emetti_suono(self):
        print('Il gatto fa Miao!')
    
    def presentati(self):
        print(f'''Il gatto di nome {self.get_nome()} e la sua eta e {self.get_eta()}
              il suo colore della pelliccia e {self.__colore_pelliccia}''')

        

print('-'*20)

animale = Animale('pippo', 25)
animale.presentati()

print('-'*20)

cane = Cane('topolino', 34, 'pastore tedesco')
cane.emetti_suono()
cane.presentati()

print('-'*20)

gatto = Getto('mini', 32, 'giallo')
gatto.presentati()
gatto.emetti_suono()