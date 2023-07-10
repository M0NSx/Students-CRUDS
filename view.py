import sqlite3

try:
  banque = sqlite3.connect('etudiant_register.db')
  print("Data base été connecter avec succès")
  
