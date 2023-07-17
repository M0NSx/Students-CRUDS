from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

from PIL import ImageTk, Image

from tkcalendar import Calendar, DateEntry
from datetime import date

from view import *

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
    l_nom = Label(frame_détails, text="Nom", height=1, anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    l_nom.place(x=4, y=10)
    e_nom = Entry(frame_détails, width=45, justify="left", relief="solid")
    e_nom.place(x=7, y=40)

    l_email = Label(frame_détails, text="Email", height=1, anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    l_email.place(x=4, y=70)
    e_email = Entry(frame_détails, width=45, justify="left", relief="solid")
    e_email.place(x=7, y=100)

    l_téléphone = Label(frame_détails, text="Téléphone", height=1, anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    l_téléphone.place(x=4, y=130)
    e_téléphone = Entry(frame_détails, width=20, justify="left", relief="solid")
    e_téléphone.place(x=7, y=160)

    l_sexe = Label(frame_détails, text="Sexe", height=1, anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    l_sexe.place(x=190, y=130)
    c_sexe = ttk.Combobox(frame_détails, width=12, font=("Ivy 8 bold"))
    c_sexe['values'] = ("Masculin","Feminine")
    c_sexe.place(x=190, y=160)

    l_date_naissance = Label(frame_détails, text="Date de naissance", height=1, anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    l_date_naissance.place(x=446, y=10)
    date_naissance = DateEntry(frame_détails, width=18, background='darkblue', foreground='white', borderwidth=2, year=2023)
    date_naissance.place(x=450, y=40)

    l_cpf = Label(frame_détails, text="CPF", height=1, anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    l_cpf.place(x=446, y=70)
    e_cpf = Entry(frame_détails, width=20, justify="left", relief="solid")
    e_cpf.place(x=450, y=100)

    les_classe = ["Classe A", "Classe B"]
    classe = []

    for i in les_classe:
        classe.append(i)

    l_classe = Label(frame_détails, text="Cours", height=1, anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    l_classe.place(x=446, y=130)
    c_classe = ttk.Combobox(frame_détails, width=20, font=("Ivy 8 bold"))
    c_classe['values'] = (classe)
    c_classe.place(x=450, y=160)

    global image, image_string, l_image

    def choisir_image():
        global image, image_string, l_image
        
        image = fd.askopenfilename()
        image_string = image
        image = Image.open(image)
        image = image.resize((130,130))
        image = ImageTk.PhotoImage(image)
        l_image = Label(frame_détails, image=image, bg=co1, fg=co4)
        l_image.place(x=300, y=10)
        
        bouton_charger['text'] = 'Changer Image'

    bouton_charger = Button(frame_détails, command=choisir_image, text="Charger image".upper(), width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7'), bg=co1, fg=co0)
    bouton_charger.place(x=300, y=160)

    l_ligne = Label(frame_détails, relief=GROOVE, text="h", height=100, anchor=NW, font=("Ivy 1"), bg=co0, fg=co0)
    l_ligne.place(x=610, y=10)
    l_ligne = Label(frame_détails, relief=GROOVE, text="h", height=100, anchor=NW, font=("Ivy 1"), bg=co1, fg=co0)
    l_ligne.place(x=608, y=10)

    l_nom1 = Label(frame_détails, text="Rechercher étudiant", height=1, anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
    l_nom1.place(x=627, y=10)
    e_nom_rechercher = Entry(frame_détails, width=17, justify="center", relief="solid", font=("Ivy 10"))
    e_nom_rechercher.place(x=630, y=35)

    bouton_rechercher = Button(frame_détails, anchor=CENTER, text="Rechercher", width=9, overrelief=RIDGE, font=("Ivy 7 bold"), bg=co1, fg=co4)
    bouton_rechercher.place(x=757, y=35)

    bouton_sauver2 = Button(frame_détails,  anchor=CENTER, text="Sauver".upper(), width=9, overrelief=RIDGE, font=("Ivy 7 bold"), bg=co3, fg=co1)
    bouton_sauver2.place(x=627, y=110)

    bouton_update2 = Button(frame_détails,  anchor=CENTER, text="Update".upper(), width=9, overrelief=RIDGE, font=("Ivy 7 bold"), bg=co6, fg=co1)
    bouton_update2.place(x=627, y=135)

    bouton_supprimer2 = Button(frame_détails, anchor=CENTER, text="Supprimer".upper(), width=9, overrelief=RIDGE, font=("Ivy 7 bold"), bg=co7, fg=co1)
    bouton_supprimer2.place(x=627, y=160)

    bouton_voir = Button(frame_détails, anchor=CENTER, text="Voir".upper(), width=9, overrelief=RIDGE, font=("Ivy 7 bold"), bg=co1, fg=co0)
    bouton_voir.place(x=727, y=160)

    def montrer_étudiants():
        app_nome = Label(frame_tableau, text="Tableau des étudiants", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # creating a treeview with dual scrollbars
        list_header = ['ID','Nom','Email','Téléphone', 'Sexe', 'Image', 'Date', 'CPF', 'Cours']

        df_list = []

        global tree_étudiants

        tree_étudiants = ttk.Treeview(frame_tableau, selectmode="extended",columns=list_header, show="headings")

        vsb = ttk.Scrollbar(frame_tableau, orient="vertical", command=tree_étudiants.yview)

        hsb = ttk.Scrollbar(frame_tableau, orient="horizontal", command=tree_étudiants.xview)

        tree_étudiants.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_étudiants.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tableau.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","nw","center", "center", "center", "center", "center", "center",]
        h=[40,150,150,70,70,70,80,80,100]
        n=0

        for col in list_header:
            tree_étudiants.heading(col, text=col.title(), anchor=NW)
            tree_étudiants.column(col, width=h[n],anchor=hd[n])

            n+=1

        for item in df_list:
            tree_étudiants.insert('', 'end', values=item)

    montrer_étudiants()

def Ajouter():
    frame_tableau_cours = Frame(frame_tableau, width=300, height=200, bg=co1)
    frame_tableau_cours.grid(row=0, column=0, pady=0, padx=10, sticky=NSEW)

    frame_tableau_ligne = Frame(frame_tableau, width=30, height=200, bg=co1)
    frame_tableau_ligne.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)

    frame_tableau_classe = Frame(frame_tableau, width=300, height=200, bg=co1)
    frame_tableau_classe.grid(row=0, column=2, pady=0, padx=10, sticky=NSEW)

    #détails du cours
    def nouveau_cours():
        nom = e_nom_cours.get()
        durée = e_durée.get()
        prix = e_prix.get()

        liste = [nom, durée, prix]

        for i in liste:
            if i == "":
                messagebox.showerror('Erreur', "Il faut remplir l'espace")
                return

        créer_cours(liste)

        messagebox.showinfo("Succès", "Tu rempli tout avec succès!")

        e_nom_cours.delete(0,END)
        e_prix.delete(0,END)
        e_durée.delete(0,END)

        montrer_cours()

    def actualiser_cours():
        try:
            tree_itens = tree_cours.focus()
            tree_dictionnaire = tree_cours.item(tree_itens)
            tree_liste = tree_dictionnaire['values']

            valeur_id = tree_liste[0]

            e_nom_cours.insert(0, tree_liste[1])
            e_durée.insert(0, tree_liste[2])
            e_prix.insert(0, tree_liste[3])

            def update():
                nom = e_nom_cours.get()
                durée = e_durée.get()

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

        vsb = ttk.Scrollbar(frame_tableau_classe, orient="vertical", command=tree_classe.yview)

        hsb = ttk.Scrollbar(frame_tableau_classe, orient="horizontal", command=tree_classe.xview)

        tree_classe.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_classe.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tableau_classe.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","e","e"]
        h=[30,130,150,80]
        n=0

        for col in list_header:
            tree_classe.heading(col, text=col.title(), anchor=NW)
            tree_classe.column(col, width=h[n],anchor=hd[n])
            
            n+=1

        for item in df_list:
            tree_classe.insert('', 'end', values=item)

    montrer_classe()

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
