from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

from PIL import ImageTk, Image

from tkcalendar import Calendar, DateEntry
from datetime import date

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
    frame_tableau_cours = Frame(frame_tableau, width=300, height=200, bg=co1)
    frame_tableau_cours.grid(row=0, column=0, pady=0, padx=10, sticky=NSEW)

    frame_tableau_ligne = Frame(frame_tableau, width=30, height=200, bg=co1)
    frame_tableau_ligne.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)

    frame_tableau_classe = Frame(frame_tableau, width=300, height=200, bg=co1)
    frame_tableau_classe.grid(row=0, column=2, pady=0, padx=10, sticky=NSEW)

    #détails du cours
    l_nom = Label(frame_détails, text="Nom du cours", height=1, anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    l_nom.place(x=4, y=10)
    e_nom_cours = Entry(frame_détails, width=35, justify="left", relief="solid")
    e_nom_cours.place(x=7, y=40)

    l_durée = Label(frame_détails, text="Durée", height=1, anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    l_durée.place(x=4, y=70)
    e_durée = Entry(frame_détails, width=20, justify="left", relief="solid")
    e_durée.place(x=7, y=100)

    l_prix = Label(frame_détails, text="Prix", height=1, anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    l_prix.place(x=4, y=130)
    e_prix = Entry(frame_détails, width=10, justify="left", relief="solid")
    e_prix.place(x=7, y=160)

    bouton_sauver1 = Button(frame_détails, anchor=CENTER, text="Sauver".upper(), width=10, overrelief=RIDGE, font=("Ivy 7"), bg=co3, fg=co1)
    bouton_sauver1.place(x=107, y=160)

    bouton_update1 = Button(frame_détails, anchor=CENTER, text="Update".upper(), width=10, overrelief=RIDGE, font=("Ivy 7"), bg=co6, fg=co1)
    bouton_update1.place(x=187, y=160)

    bouton_supprimer1 = Button(frame_détails, anchor=CENTER, text="Supprimer".upper(), width=10, overrelief=RIDGE, font=("Ivy 7"), bg=co7, fg=co1)
    bouton_supprimer1.place(x=267, y=160)

    def montrer_cours():
        app_nome = Label(frame_tableau_cours, text="Tableau du cours", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        list_header = ['ID','Cours','Durée','Prix']

        df_list = []

        global tree_cours

        tree_cours = ttk.Treeview(frame_tableau_cours, selectmode="extended",columns=list_header, show="headings")

        vsb = ttk.Scrollbar(frame_tableau_cours, orient="vertical", command=tree_cours.yview)

        hsb = ttk.Scrollbar(frame_tableau_cours, orient="horizontal", command=tree_cours.xview)

        tree_cours.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_cours.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tableau_cours.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","e","e"]
        h=[30,150,80,60]
        n=0

        for col in list_header:
            tree_cours.heading(col, text=col.title(), anchor=NW)
            tree_cours.column(col, width=h[n],anchor=hd[n])

            n+=1

        for item in df_list:
            tree_cours.insert('', 'end', values=item)

    montrer_cours()

    #séparateur de ligne
    l_ligne = Label(frame_détails, relief=GROOVE, text="h", height=100, anchor=NW, font=("Ivy 1"), bg=co0, fg=co0)
    l_ligne.place(x=374, y=10)
    l_ligne = Label(frame_détails, relief=GROOVE, text="h", height=100, anchor=NW, font=("Ivy 1"), bg=co1, fg=co0)
    l_ligne.place(x=372, y=10)

    l_ligne = Label(frame_tableau_ligne, relief=GROOVE, text="h", height=140, anchor=NW, font=("Ivy 1"), bg=co0, fg=co0)
    l_ligne.place(x=6, y=10)
    l_ligne = Label(frame_tableau_ligne, relief=GROOVE, text="h", height=140, anchor=NW, font=("Ivy 1"), bg=co1, fg=co0)
    l_ligne.place(x=4, y=10)

    #détails du classe
    l_nom = Label(frame_détails, text="Nom du classe", height=1, anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    l_nom.place(x=404, y=10)
    e_nom_classe = Entry(frame_détails, width=35, justify="left", relief="solid")
    e_nom_classe.place(x=407, y=40)

    l_classe = Label(frame_détails, text="Cours", height=1, anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    l_classe.place(x=404, y=70)

    les_cours = ["cours1", "cours2"]
    cours = []

    for i in les_cours:
        cours.append(i)

    c_cours = ttk.Combobox(frame_détails, width=20, font=("Ivy 8 bold"))
    c_cours['values'] = (cours)
    c_cours.place(x=407, y=100)

    l_date_initiale = Label(frame_détails, text="Date initiale", height=1, anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    l_date_initiale.place(x=406, y=130)
    date_initiale = DateEntry(frame_détails, width=10, background='darkblue', foreground='white', borderwidth=2, year=2023)
    date_initiale.place(x=407, y=160)

    bouton_sauver2 = Button(frame_détails, anchor=CENTER, text="Sauver".upper(), width=10, overrelief=RIDGE, font=("Ivy 7"), bg=co3, fg=co1)
    bouton_sauver2.place(x=507, y=160)

    bouton_update2 = Button(frame_détails, anchor=CENTER, text="Update".upper(), width=10, overrelief=RIDGE, font=("Ivy 7"), bg=co6, fg=co1)
    bouton_update2.place(x=587, y=160)

    bouton_supprimer2 = Button(frame_détails, anchor=CENTER, text="Supprimer".upper(), width=10, overrelief=RIDGE, font=("Ivy 7"), bg=co7, fg=co1)
    bouton_supprimer2.place(x=667, y=160)

    def montrer_classe():
        app_nome = Label(frame_tableau_classe, text="Tableau du classe", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # creating a treeview with dual scrollbars
        list_header = ['ID','Nom du classe','Cours','Date initiale']

        df_list = []

        global tree_classe

        tree_classe = ttk.Treeview(frame_tableau_classe, selectmode="extended",columns=list_header, show="headings")

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
app_img_registre = app_img_registre.resize((18,18))
app_img_registre = ImageTk.PhotoImage(app_img_registre)
app_registre = Button(frame_données, command=lambda:control('Registre'), image=app_img_registre, text="Registre", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_registre.place(x=10, y=30)

app_img_ajouter = Image.open('add_logo.png')
app_img_ajouter = app_img_ajouter.resize((18,18))
app_img_ajouter = ImageTk.PhotoImage(app_img_ajouter)
app_ajouter = Button(frame_données, command=lambda:control('Ajouter'), image=app_img_ajouter, text="Ajouter", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_ajouter.place(x=123, y=30)

app_img_sauver = Image.open('save_logo.png')
app_img_sauver = app_img_sauver.resize((18,18))
app_img_sauver = ImageTk.PhotoImage(app_img_sauver)
app_sauver = Button(frame_données, command=lambda:control('Sauver'), image=app_img_sauver, text="Sauver", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_sauver.place(x=236, y=30)

fenêtre.mainloop()
