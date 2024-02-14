# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 12:36:43 2024

@author: michelra
"""

# Génération de la base de données du stock
#Import de la fonction de push dans la base de données et des données du stock
from fonctions import sql_execute
from classes.class_stock import stock, importer, csv_import


# Création de la table Stock
sql_create_table_stock = """
CREATE TABLE stock (
    identifiant       INTEGER   NOT NULL  PRIMARY KEY,
	nom               TEXT      NOT NULL,
	description       TEXT      NOT NULL,
	conditionnement   TEXT      NOT NULL,
    quantite          INTEGER   NOT NULL,
	prix              INTEGER   NOT NULL,
	adresseImage      TEXT      NOT NULL,
	visibility        BOOLEAN   NOT NULL
);"""

# sql_execute(sql_insert = sql_create_table_stock)



# Remplissage de la table Stock

# Fonction de chargement du CSV
assert importer(csv_import) == True, "L'importation du stock contient une erreur de chargement."

# Parcours du stock et ajout dans la base
# for element in stock:
#     sql_request = f"""INSERT INTO stock VALUES (
#   {stock[element].getId()},
#   "{stock[element].getName()}",
#   "{stock[element].getDescription()}",
#   "{stock[element].getConditionnement()}",
#   {stock[element].getQuantite()},
#   {stock[element].getPrix()},
#   "{stock[element].getAdresseImage()}",
#   {stock[element].getVisibility()});"""
#     sql_execute(sql_request)