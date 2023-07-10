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
