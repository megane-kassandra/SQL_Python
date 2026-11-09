import sqlite3
from pathlib import Path

def ouvrir_connexion(chemin_db):
    if not Path(chemin_db).exists():
        raise FileNotFoundError("La base de donnees n'existe pas")
    else:
        conn = sqlite3.connect("gestion_aeroports.db")      
        return conn