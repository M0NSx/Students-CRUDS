import sqlite3

try:
  banque = sqlite3.connect('etudiant_register.db')
  print("Data base été connecter avec succès")
except sqlite3.Error as erreur:
  print("Il n'a pas été possible de se connecter dans data base", erreur)

def créer_cours(i):
    with banque:
        cur = banque.cursor()
        query = "INSERT INTO courses (nom, durée, prix) VALUES (?,?,?)"
        cur.execute(query, i)

#créer_cours(['Python','cinq semaines', 60])

def voir_cours():
    liste = []
    with banque:
        cur = banque.cursor()
        cur.execute('SELECT * FROM courses')
        ligne = cur.fetchall()
        for i in ligne:
            liste.append(i)
    return liste

#print(voir_cours())

def update_cours(i):
    with banque:
        cur = banque.cursor()
        query = "UPDATE courses SET nom=?, durée=?, prix=?, WHERE id=?"
        cur.execute(query, i)

liste = ['Python','cinq semaines', 60, 1]

def supprimer_cours(i):
    with banque:
        cur = banque.cursor()
        query = "DELETE FROM courses WHERE id=?"
        cur.execute(query, i)

#supprimer_cours([7])

#Tableau de classes
def créer_classes(i):
    with banque:
        cur = banque.cursor()
        query = "INSERT INTO classes (nom, course_nom, initiale_date) VALUES (?,?,?)"
        cur.execute(query, i)

def voir_classes():
    liste = []
    with banque:
        cur = banque.cursor()
        cur.execute('SELECT * FROM classes')
        ligne = cur.fetchall()

        for i in ligne:
            liste.append(i)
    return liste

def update_classes(i):
    with banque:
        cur = banque.cursor()
        query = "UPDATE classes SET nom=?, course_nom=?, nitiale_date=?, WHERE id=?"
