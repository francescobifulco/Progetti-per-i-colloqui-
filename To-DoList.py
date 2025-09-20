"""Progetto 1: "To-Do List" da riga di comando 📝
Questo progetto è ideale per i principianti e si concentra sulle basi 
di Python: variabili, liste, cicli for e while, e funzioni. 
Lo scopo è creare un'applicazione interattiva che permette 
all'utente di aggiungere, visualizzare e rimuovere compiti da una lista.

Concetti chiave:
Strutture dati: Utilizzerai una lista per salvare i compiti.

Input/Output (I/O): Imparerai a prendere input dall'utente (input()) 
e a stampare output (print()).

Controllo di flusso: Userai un ciclo while per mantenere 
il programma in esecuzione finché l'utente non decide di uscire, 
e istruzioni if/elif/else per gestire le diverse opzioni 
(aggiungere, visualizzare, rimuovere)."""

to_do_list = []

def aggiungi():
    oggetto = input('Aggiungi un elemento nella lista: ')
    to_do_list.append(oggetto)
    print(f'Hai aggiunto alla tua lista elemento: {oggetto}')

def visualizza():
    if not to_do_list:
        print('La lista e vuota')
    else:
        for indice in to_do_list:
            print(f'Il contenuto della tua lista e: {indice}')

def rimuovi():
    while True:
        if not to_do_list:
            print('La lista e vuota')
            break
        else:
            for indice in to_do_list:
                print(f'Il contenuto della tua lista e: {indice}')
        
        scelta = input('scegli elemento da rimuovere nella lista:')
        if not scelta:
            print(f'{scelta} elemento non trovato')
        elif scelta in to_do_list:
            to_do_list.remove(scelta)
            print(f'Elemento {scelta} e stato rimosso con successo!') 

print('Benvenuto nella tua To-do Lista!')

scelta = ''

while True:
    print('Cosa vuoi fare!')
    scelta = input('[A]ggiungi \n[V]isualizzare \n[R]imuovere \n[E]sci \n').lower()
    if scelta == 'e':
        break
    if scelta == 'a':
        aggiungi()
    elif scelta == 'v':
        visualizza()
    elif scelta == 'r':
        rimuovi()
        
        
print('Sei usci dalla tua lista ARRIVEDERCI')