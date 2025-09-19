"""
Progetto 1: Calcolatrice Semplice 🧮
Questo è un progetto classico per chiunque inizi a programmare con le GUI. Ti aiuta a capire come funzionano i widget di base come bottoni e caselle di testo, 
e come gestire gli eventi (il "click" di un bottone).

Passaggi chiave:
Crea la finestra principale: Utilizza tkinter.Tk() per creare la finestra dell'applicazione.

Aggiungi i widget: Includi una casella di testo (un Entry widget) per mostrare i numeri e i risultati, e diversi bottoni (Button widget) per i numeri e gli operatori.

Gestisci la logica: Scrivi una funzione che venga chiamata ogni volta che si preme un bottone. Questa funzione deve aggiornare la casella di testo e calcolare il risultato.

Questo progetto ti insegna la gestione degli eventi e il layout di base dei widget.
"""
# Importiamo le librerie necessarie da tkinter
from tkinter import *
from tkinter import ttk

# Creiamo la finestra principale dell'applicazione (la radice del nostro programma)
root = Tk()

root.title('Calcolatrice Semplice')

# Imposta la dimensione minima della finestra che l'utente può raggiungere
root.minsize(width=470, height=400)

# Imposta la dimensione massima della finestra che l'utente può raggiungere
root.maxsize(width=470, height=400)

# Sposta la finestra in primo piano, portandola sopra le altre finestre
root.lift()

# Variabili globali per memorizzare i numeri e l'operazione
first_number = ""
second_number = ""
operation = ""

# Etichetta per mostrare l'input e il risultato
display = Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid', justify='right')
display.grid(row=0, column=0, columnspan=4)

# Funzione generica per tutti i pulsanti numerici e operazioni
def buttonPressed(number):
    global first_number, second_number, operation

    if number.isdigit():  # Se è un numero
        if operation == "":
            first_number += number  # Aggiungi al primo numero
            display.delete(0, END)  # Cancella il display
            display.insert(0, first_number)  # Mostra il primo numero
        else:
            second_number += number  # Aggiungi al secondo numero
            display.delete(0, END)
            display.insert(0, second_number)  # Mostra il secondo numero

    elif number == 'C':  # Se è il tasto cancella
        first_number = ""
        second_number = ""
        operation = ""
        display.delete(0, END)

    elif number in ['+', '-', '*', '/']:  # Se è un operatore
        operation = number  # Salva l'operazione
        display.delete(0, END)
        display.insert(0, first_number + " " + operation)  # Mostra il numero e l'operatore

    elif number == '=':  # Se è il tasto uguale
        if first_number and second_number and operation:
            # Esegui il calcolo
            if operation == '+':
                result = float(first_number) + float(second_number)
            elif operation == '-':
                result = float(first_number) - float(second_number)
            elif operation == '*':
                result = float(first_number) * float(second_number)
            elif operation == '/':
                if second_number != "0":
                    result = float(first_number) / float(second_number)
                else:
                    result = "Errore"  # Gestisci la divisione per zero
            display.delete(0, END)
            display.insert(0, result)  # Mostra il risultato
            first_number = str(result)  # Salva il risultato per eventuali operazioni successive
            second_number = ""
            operation = ""

# Crea i pulsanti da 1 a 9 e le operazioni
buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('0', 4, 1), ('=', 4, 2), ('C', 4, 0),
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3)
]

# Aggiungi i pulsanti alla finestra
for text, row, column in buttons:
    button = ttk.Button(root, text=text, command=lambda num=text: buttonPressed(num))
    button.grid(row=row, column=column, ipadx=20, ipady=20)

root.mainloop()  # Avvia il "loop" principale di Tkinter