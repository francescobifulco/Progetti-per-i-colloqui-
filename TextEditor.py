"""Progetto 2: Semplice Text Editor 📝
Questo progetto è un passo avanti rispetto alla calcolatrice. 
Ti permette di esplorare widget più avanzati come l'area di testo 
multilinea (Text widget) e di interagire con il file system del tuo 
computer (aprire e salvare file).

Passaggi chiave:
Crea un'area di testo: Usa Text per l'area principale in cui l'utente 
scriverà.

Crea un menù: Utilizza Menu per aggiungere opzioni come "Apri", 
"Salva" e "Esci".

Implementa le funzionalità: Scrivi le funzioni per aprire una 
finestra di dialogo per i file, leggere il contenuto di un file e 
caricarlo nell'area di testo, e salvare il contenuto dell'area di 
testo in un nuovo file.

Questo progetto ti introduce al concetto di menù a tendina e 
all'interazione con i file, competenze cruciali per molte 
applicazioni desktop."""

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

# Creiamo la finestra principale dell'applicazione (la radice del nostro programma)
root = Tk()

root.title('Semplice Text Editor')

# Imposta la dimensione minima della finestra che l'utente può raggiungere
root.minsize(400, 100) 
root.geometry("600x400")

# Imposta la dimensione massima della finestra che l'utente può raggiungere
root.maxsize(1000, 1000) 

# Sposta la finestra in primo piano, portandola sopra le altre finestre
root.lift()

def apri_file():
     file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("File di testo", "*.txt"), ("Tutti i file", "*.*")]
    )
     if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                contenuto = file.read()
                text_area.delete(1.0, END)
                text_area.insert(END, contenuto)
        except Exception as e:
            messagebox.showerror("Errore", f"Errore nell'apertura del file:\n{e}")

# Funzione per salvare un file
def salva_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("File di testo", "*.txt"), ("Tutti i file", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                contenuto = text_area.get(1.0, END)
                file.write(contenuto)
        except Exception as e:
            messagebox.showerror("Errore", f"Errore nel salvataggio del file:\n{e}")


menubar = Menu(root)

# Colleghiamo la barra dei menu alla finestra principale.
root.config(menu=menubar)

# Creiamo un menu a tendina. 'tearoff=0' rimuove la linea tratteggiata in alto,
# che permette di "staccare" il menu dalla finestra.
file_menu = Menu(menubar, tearoff=0)

# Aggiungiamo comandi al menu 'File'. Ogni comando ha un'etichetta e una funzione da eseguire.
# In questo caso, 'root.quit' chiude l'applicazione.
file_menu.add_command(label='Salva', command=salva_file)
file_menu.add_command(label='Apri', command=apri_file)

# Aggiungiamo un separatore orizzontale per organizzare visivamente il menu.
file_menu.add_separator()

# Aggiungiamo un altro comando che chiude l'applicazione.
file_menu.add_command(label='Esci', command=root.quit)

# Aggiungiamo il menu 'File' alla barra dei menu principale.
menubar.add_cascade(label='File', menu=file_menu)

text_area = Text(root, wrap=WORD, font=("Helvetica", 12))
text_area.pack(expand=True, fill=BOTH, padx=10, pady=5)

root.mainloop() # Avvia il "loop" principale di Tkinter.