# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 12:12:19 2024

@author: michelra
"""

# Import du module MySQL
import mysql.connector

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
username = ""
password = ""
database = "projet_magasin"
port = 3306

# Connexion à la base de données
connexion = connect_to_database(host, port, username, password, database)


def sql_execute(sql_insert):
    # Création d'un curseur pour exécuter des requêtes SQL
    cursor = connexion.cursor()
    
    # Requête SQL pour insérer des données dans la table
    # sql_insert = f"INSERT INTO {table} ({colonnes}) VALUES ({values})"
    
    try:
        # Exécution de la requête pour chaque ensemble de données
        cursor.execute(sql_insert)
    
        # Validation des changements dans la base de données
        connexion.commit()
        print("Données insérées avec succès !")
        return True
    
    except mysql.connector.Error as err:
        # En cas d'erreur, annulation des modifications
        connexion.rollback()
        return False
        print(f"Erreur lors de l'insertion des données : {err}")
    
    finally:
        # Fermeture du curseur et de la connexion
        cursor.close()
        connexion.close()
        
def sql_execute_select(sql_insert):
    # Création d'un curseur pour exécuter des requêtes SQL
    cursor = connexion.cursor()
    
    # Requête SQL pour insérer des données dans la table
    # sql_insert = f"INSERT INTO {table} ({colonnes}) VALUES ({values})"
    
    try:
        # Exécution de la requête pour chaque ensemble de données
        cursor.execute(sql_insert)
    
        # Récupération des données
        result = cursor.fetchall()
        return result
    
    except mysql.connector.Error as err:
        # En cas d'erreur, annulation des modifications
        connexion.rollback()
        return False
        print(f"Erreur lors de la récupération des données : {err}")
    
    finally:
        # Fermeture du curseur et de la connexion
        cursor.close()
        connexion.close()

def insert_into(table, colonnes, values):
    # Création d'un curseur pour exécuter des requêtes SQL
    cursor = connexion.cursor()
    
    # Requête SQL pour insérer des données dans la table
    sql_insert = f"INSERT INTO {table} ({colonnes}) VALUES ({values})"
    
    try:
        # Exécution de la requête pour chaque ensemble de données
        cursor.execute(sql_insert)
    
        # Validation des changements dans la base de données
        connexion.commit()
        print("Données insérées avec succès !")
    
    except mysql.connector.Error as err:
        # En cas d'erreur, annulation des modifications
        connexion.rollback()
        print(f"Erreur lors de l'insertion des données : {err}")
    
    finally:
        # Fermeture du curseur et de la connexion
        cursor.close()
        connexion.close()

"""
def insert_into(table, colonnes, values):
    # Création d'un curseur pour exécuter des requêtes SQL
    cursor = connexion.cursor()
    
    # Requête SQL pour insérer des données dans la table
    sql_insert = f"INSERT INTO {table} ({colonnes}) VALUES ({values})"
    
    try:
        # Exécution de la requête pour chaque ensemble de données
        cursor.executemany(sql_insert)
    
        # Validation des changements dans la base de données
        cursor.commit()
        print("Données insérées avec succès !")
    
    except mysql.connector.Error as err:
        # En cas d'erreur, annulation des modifications
        cursor.rollback()
        print(f"Erreur lors de l'insertion des données : {err}")
    
    finally:
        # Fermeture du curseur et de la connexion
        cursor.close()
        # connexion.close()
"""