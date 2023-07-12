from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

from PIL import ImageTk, Image

# couleurs
co0 = "#2e2d2b"  # noir
co1 = "#feffff"  # blanc 
co2 = "#e5e5e5"  # gris
co3 = "#00a095"  # vert
co4 = "#403d3d"   # lettre
co6 = "#003452"   # bleu
co7 = "#ef5350"   # rouge

co6 = "#038cfc"   # bleu
co8 = "#263238"   # + vert
co9 = "#e9edf5"   # + vert

#créer fenêtre
fenêtre = Tk()
fenêtre.title("")
fenêtre.geometry("850x620")
fenêtre.configure(background=co1)
fenêtre.resizable(width=FALSE, height=FALSE)
style = Style(fenêtre)
style.theme_use("clam")

# Créer Frames
frame_logo = Frame(fenêtre, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)
ttk.Separator(fenêtre, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_donnés = Frame(fenêtre, width=850, height=65, bg=co1)
frame_donnés.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(fenêtre, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_détails = Frame(fenêtre, width=850, height=200, bg=co1)
frame_détails.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tableau = Frame(fenêtre, width=850, height=200, bg=co1)
frame_tableau.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)

app_logo = Image.open('étudiant_logo.png')
app_logo = app_logo.resize((50,50))
app_logo = ImageTk.PhotoImage(app_logo)
app_lg = Label(frame_logo, image=app_logo, text="Registre des étudiants", width=850, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=co6, fg=co1)
app_lg.place(x=0, y=0)

def Étudiants():
    print("Étudiant")

def Ajouter():
    print("Cours et classes")

def Sauver():
    print("Sauver")

def control(i):
    if i == 'Registre':
        for widget in frame_détails.winfo_children():
            widget.destroy()

        for widget in frame_tableau.winfo_children():
            widget.destroy()

        Étudiants()

    if i == 'Ajouter':
        for widget in frame_détails.winfo_children():
            widget.destroy()

        for widget in frame_tableau.winfo_children():
            widget.destroy()

        Ajouter()

    if i == 'Sauver':
        for widget in frame_détails.winfo_children():
            widget.destroy()

        for widget in frame_tableau.winfo_children():
            widget.destroy()

        Sauver()

app_img_registre = Image.open('add_logo.png')

fenêtre.mainloop()
