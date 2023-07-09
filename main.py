import sqlite3

try:
      banque = sqlite3.connect('etudiant_register.db')
      print("Data base été connecter avec succès")
except sqlite3.Error as erreur:
    print("Il n'a pas été possible de se connecter dans data base", erreur)

try:
    with banque:
        cur = banque.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS courses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            durée TEXT,
            prix REAL
        )""")


        print("Table courses créé avec succès")
except sqlite3.Error as erreur:
    print("il n'a pas été possible de se créé la table courses", erreur)

try:
    with banque:
