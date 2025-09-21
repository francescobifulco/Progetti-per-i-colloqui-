"""Progetto 2: Analizzatore di Testo 📊
Questo progetto ti introduce alla manipolazione delle stringhe, 
alla gestione dei file e all'uso dei dizionari. 
L'obiettivo è creare un programma che legge un file 
di testo e ne analizza il contenuto, calcolando, ad esempio, 
il numero di parole, la frequenza di ogni parola e 
la lunghezza media delle parole.

Concetti chiave:
Gestione dei file: Dovrai aprire, leggere e chiudere un file 
(with open(...) as file:).

Stringhe e metodi: Userai metodi come .split() e .lower() 
per elaborare il testo.

Dizionari: Un dizionario è perfetto per contare la frequenza 
delle parole,
mappando ogni parola al suo conteggio.
"""

testo = input("inserisci un testo: ")

with open("mio_file.txt", "w") as file:
    file.write(testo)
    
with open("mio_file.txt", "r") as file:
    contenuto = file.read()
    print(contenuto)
    
lunghezza_testo = len(contenuto)
print(f'la lunghezza del testo e: {lunghezza_testo}')

lista_parole = contenuto.split()
print(f'il numero di parole e: {len(lista_parole)}')

def contare(contenuto):
    contenuto = contenuto.lower()
    lista_testo = contenuto.split()
    frequenza = {}
    for parole in lista_testo:
        if parole in frequenza:
            frequenza[parole] += 1
        else:
            frequenza[parole] = 1
    print("Frequenza delle parole:\n")
    for parola in sorted(frequenza):
        print(f"La parola '{parola}' compare {frequenza[parola]} volte.")
    
contare(contenuto)

def lunghezza_media(contenuto):
    lista_testo = contenuto.split()
    somma = 0
    for parola in lista_testo:
        somma += len(parola)
    dividi = (somma / len(lista_testo))
    print(f'la lunghezza media e: {dividi:.2f}')

lunghezza_media(contenuto)