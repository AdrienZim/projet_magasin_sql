# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 12:22:14 2023

@author: michelra
"""
# Import du module Tkinter, sys et mysql.connector
import tkinter as tk
from tkinter import ttk
import sys
import mysql.connector

# Imports des fichiers de Classe & de la fonction d'interrogation de la base de données -> sql_execute
from fonctions import sql_execute
from classes.class_stock import *
from interfaces.client_affichage_stock import main_client

# Test de la présence du Package mysql.connector
print("version mysql :", mysql.connector.__version__)

# Connexion à la base de donnée

def connect_to_database(host, port, username, password, database):
    try:
        # Connexion à la base de données MySQL
        conn = mysql.connector.connect(
            host = host,
            user = username,
            password = password,
            database = database,
            port = port
        )
        
        if conn.is_connected():
            print("Connecté à la base de données MySQL")
            return conn
        else:
            print("Impossible de se connecter à la base de données")
            return None
    except mysql.connector.Error as e:
        print("Erreur de connexion à la base de données:", e)
        return None

# Paramètres de connexion à la base de données
host = "jp2.dmsv-manche.fr"
username = "michelra"
password = "Soky8390"
database = "projet_magasin"
port = 3306

# Connexion à la base de données
connexion = connect_to_database(host, port, username, password, database)


# Fonction de chargement du CSV
assert sql_execute("SELECT * FROM stock;") == True, "L'importation du stock contient une erreur de chargement."

# Fonctions :
def action(event):
	# Obtenir l'élément sélectionné
    select = menu_choix_interface.get()
    
    if select == "Client":
        app.destroy()
        main_client()
    
    if select == "Gestionnaire du stock":
        print(None)
    
    if select == "Fermeture" :
        app.destroy()
        connexion.close()
        sys.exit("Fermeture de l'interface")


# Création de la page Tkinter et définition de sa taille
app = tk.Tk()
app.title("Choix de l'interface")
app.geometry('900x600')

# Choix de l'interface et définition du menu sur "Client" par défault
labelChoix = tk.Label(app, text = "Veuillez choisir votre interface !")
interfaces_possibles = ["Client", "Gestionnaire du stock", "Fermeture"]
menu_choix_interface = ttk.Combobox(app, values = interfaces_possibles)
# menu_choix_interface.current(0)


# Affichages dans l'interface
labelChoix.pack()
menu_choix_interface.pack()
# Détection du choix
menu_choix_interface.bind("<<ComboboxSelected>>", action)

# Lancement de l'interface
app.mainloop()