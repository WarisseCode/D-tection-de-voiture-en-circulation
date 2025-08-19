import sqlite3
#Se connecter à la base de données SQLite (ou la créer si elle n'existe pas)
conn = sqlite3.connect('licensePlatesDatabase.db')

#Créer un objet curseur pour interagir avec la base de données
cursor = conn.cursor()


#Créer une table pour stocker les données des plaques d'immatriculation

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS LicensePlates(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        start_time TEXT,
        end_time TEXT,
        license_plate TEXT
    )
    '''
)