# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 11:58:45 2023

@author: michelra
"""

# Import de la fonction sql_execute
from fonctions import sql_execute, sql_execute_select

# Définition du dictionnaire de stock
stock = {}

# Définition de la classe Stock
class Stock:
    def __init__(self, id_article: int, product_name: str, description: str, quantite: int, prix: int, conditionnement: str, adresse_image: str, visibility: bool):
        """
        Initialisation d'un objet de type Stock

        Parameters
        ----------
        id_article : int
            Numéro de l'article dans le stock.
        product_name : str
            Nom du produit.
        description : str
            Description du produit.
        quantite : int
            Nombre de cet article disponible.
        prix : int
            Prix de l'article.
        conditionnement : str
            Conditionnement de l'article.
        adresse_image : str
            Adresse UNC de l'image.
        visibility : bool
            Définit si l'article est visible pour les clients - Défault : True.

        Returns
        -------
        None.

        """
        self.id = id_article
        self.name = product_name
        self.description = description
        self.quantite = quantite
        self.prix = prix
        self.conditionnement = conditionnement
        self.adresse_image = adresse_image
        self.visibility = visibility
        
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
        
    def getDescription(self):
        return self.description
    
    def getQuantite(self):
        return self.quantite
    
    def getPrix(self):
        return self.prix
    
    def getConditionnement(self):
        return self.conditionnement
    
    def getAdresseImage(self):
        return self.adresse_image
    
    def getVisibility(self):
        return self.visibility
    
    def modifier_produit(self, id_article: int, product_name: str, description: str, quantite: int, prix: int, conditionnement: str, adresse_image: str, visibility: bool):
        """
        Permet de modifier entièrement un produit.

        Parameters
        ----------
        id_article : int
            Numéro de l'article dans le stock.
        product_name : str
            Nom du produit.
        description : str
            Description du produit.
        quantite : int
            Nombre de cet article disponible.
        prix : int
            Prix de l'article.
        conditionnement : str
            Conditionnement de l'article.
        adresse_image : str
            Adresse UNC de l'image.
        visibility : bool
            Définit si l'article est visible pour les clients - Défault : True.

        Returns
        -------
        str
            Article enregistré ou l'article n'est pas dans le stock.

        """
        if id_article in stock.keys():
            stock[int(id_article)] = Stock(int(id_article), str(product_name), str(description), int(quantite), int(prix), str(conditionnement), str(adresse_image), bool(visibility))
            sql_request = f"""
            UPDATE  stock
            SET    (identifiant       = {int(id_article)},
                    nom               = {str(product_name)},
                    description       = {str(description)},
                    conditionnement   = {str(conditionnement)},
                    quantite          = {int(quantite)},
                    prix              = {int(prix)},
                    adresseImage      = {str(adresse_image)},
                    visibility        = {bool(visibility)})
            WHERE   identifiant       = {int(id_article)}
            ;"""
            assert sql_execute(sql_request) == True, "L'export du stock ne s'est pas passé comme prévu."
            return "Les modifications de l'article ont bien été enregistrées."
        else : return "L'article que vous souhaitez modifier n'est pas dans le stock."
    
    def augmenter_produit(self):
        """
        Permet d'augmenter la quantité du produit à vendre de 1.

        Returns
        -------
        str
            Article enregistré ou l'article n'est pas dans le stock.

        """
        if self.id in stock.keys():
            sql_request = f"""
            UPDATE stock
            SET    quantite += 1
            WHERE  identifiant = {self.id};"""
            assert sql_execute(sql_request) == True, "L'enregistrement du stock ne s'est pas passé comme prévu."
            obj = stock[int(self.id)]
            obj.quantite += 1
            return "Les modifications de l'article ont bien été enregistrées."
        else : return "L'article que vous souhaitez modifier n'est pas dans le stock."

    def soustraire_produit(self):
        """
        Permet de diminuer la quantité du produit à vendre de 1.

        Returns
        -------
        str
            Article enregistré ou l'article n'est pas dans le stock.

        """
        if self.id in stock.keys():
            sql_request = f"""
            UPDATE stock
            SET    quantite -= 1
            WHERE  identifiant = {self.id};"""
            assert sql_execute(sql_request) == True, "L'enregistrement du stock ne s'est pas passé comme prévu."
            obj = stock[int(self.id)]
            obj.quantite -= 1
            return "Les modifications de l'article ont bien été enregistrées."
        else : return "L'article que vous souhaitez modifier n'est pas dans le stock."
        
    
    def cacher(self):
        """
        Permet de modifier la valeur de l'enregistrement pour l'affichage dans l'interface client.

        Returns
        -------
        str
            Article enregistré ou l'article n'est pas dans le stock.

        """
        if self.id in stock.keys():
            # Si visibility est sur TRUE
            obj = stock[int(self.id)]
            if obj.visibility == True :
                sql_request_true = f"""
                UPDATE stock
                SET    visibility = 0
                WHERE  identifiant = {self.id};"""
                assert sql_execute(sql_request_true) == True, "L'enregistrement du stock ne s'est pas passé comme prévu."
                obj.visibility = False
                return "Les modifications de l'article ont bien été enregistrées."
            
            # Si visibility est sur FALSE
            elif obj.visibility == False :
                sql_request_true = f"""
                UPDATE stock
                SET    visibility = 1
                WHERE  identifiant = {self.id};"""
                assert sql_execute(sql_request_true) == True, "L'enregistrement du stock ne s'est pas passé comme prévu."
                obj.visibility = True
                return "Les modifications de l'article ont bien été enregistrées."

        else : return "L'article que vous souhaitez modifier n'est pas dans le stock."

def ajouter_au_stock(id_article: int, product_name: str, description: str, quantite: int, prix: int, conditionnement: str, adresse_image: str, visibility: bool):
    """
    Permet d'ajouter un article au stock avec un numéro qui n'existe pas dans le stock.

    Parameters
    ----------
    id_article : int
        Numéro de l'article dans le stock.
    product_name : str
        Nom du produit.
    description : str
        Description du produit.
    quantite : int
        Nombre de cet article disponible.
    prix : int
        Prix de l'article.
    conditionnement : str
        Conditionnement de l'article.
    adresse_image : str
        Adresse UNC de l'image.
    visibility : bool
        Définit si l'article est visible pour les clients - Défault : True.

    Returns
    -------
    str
        Article enregistré ou l'article n'est pas dans le stock.

    """
    if id_article not in stock.keys():
        stock[int(id_article)] = Stock(int(id_article), str(product_name), str(description), int(quantite), int(prix), str(conditionnement), str(adresse_image), bool(visibility))
        sql_request = f"""
        INSERT INTO stock
        VALUES (identifiant       = {int(id_article)},
                nom               = {str(product_name)},
                description       = {str(description)},
                conditionnement   = {str(conditionnement)},
                quantite          = {int(quantite)},
                prix              = {int(prix)},
                adresseImage      = {str(adresse_image)},
                visibility        = {bool(visibility)});"""
        assert sql_execute(sql_request) == True, "L'enregistrement du stock ne s'est pas passé comme prévu."
        
        return "Les modifications de l'article ont bien été enregistrées."
    else : return "L'article que vous souhaitez modifier est déjà dans le stock."

def importer() -> bool:
    """
    Permet de charger dans le stock les informations contenues dans le CSV.

    Parameters
    ----------
    fichier_csv : str
        Chemin UNC relatif du fichier CSV.

    Returns
    -------
    bool
        Renvoie True si l'import s'est bien passé.

    """
    rows = sql_execute_select("SELECT * FROM stock;")
    for row in rows :
        stock[int(row[0])] = Stock(id_article=int(row[0]), product_name=row[1], description=row[2], conditionnement=str(row[3]), quantite=int(row[4]), prix=int(row[5]), adresse_image=str(row[6]), visibility=bool(row[7]))
    return True


# def convert(objet: dict) -> dict :
#     """
#     Permet de convertir le Stock en dictionnaire unique.

#     Parameters
#     ----------
#     objet : dict
#         Dictionnaire du stock.

#     Returns
#     -------
#     dict

#     """
#     return {"Identifiant": int(stock[objet].id), "product_name_fr": stock[objet].name, "generic_name_fr": stock[objet].description, "quantity": stock[objet].conditionnement, "Prix": int(stock[objet].prix), "adresse_image": stock[objet].adresse_image, "nombre": int(stock[objet].quantite), "visibility": bool(stock[objet].visibility)}

# def exporter(fichier_csv: str, contenu: dict) -> bool:
#     """
#     Exporter les données du dictionnaire stock dans un CSV.

#     Parameters
#     ----------
#     fichier_csv : str
#         Chemin UNC relatif du fichier CSV.
#     contenu : dict
#         Dictionnaire du stock.

#     Returns
#     -------
#     bool
#         Renvoie True si l'export s'est bien passé.

#     """
#     table_valide = [convert(obj) for obj in stock]
        
#     with open(fichier_csv, mode="w", encoding="utf8", newline='') as sortie:
#         objet = csv.DictWriter(sortie, fieldnames=["Identifiant", "product_name_fr", "generic_name_fr", "quantity", "Prix", "adresse_image", "nombre", "visibility"], delimiter=";")
#         objet.writeheader()
#         objet.writerows(table_valide)
#         return True


def search_num_article(nom: str) -> int:
    """
    Fonction pour rechercher un numéro d'article dans le dictionnaire stock

    Parameters
    ----------
    nom : str
        Nom de l'article à rechercher dans le dictionnaire stock.

    Returns
    -------
    int
        Numéro de l'article dans le dictionnaire stock.
    """
    for element in stock:
        if stock[element].getName() == nom:
            return stock[element].getId()


###################################################################
######################### Tests unitaires #########################
###################################################################

# lol = stock[1]
# # .modifier_produit()
# print(".modifier_produit()", lol.modifier_produit(1, "Purée de Tomates", "Purée de lol", 4, 11, "400.0 g", "Mutti", False))

# # .augmenter_produit()
# print(".augmenter_produit()", lol.augmenter_produit())

# # .soustraire_produit()
# print(".soustraire_produit()", lol.soustraire_produit())

# # .ajouter()
# print("ajouter_au_stock()", ajouter_au_stock(28, "Je suis un objet", "Objet de type objet", 4, 11, "500.0 g", "pas d'adresse", False))
# print(stock[28].id, stock[28].name, stock[28].description, stock[28].quantite, stock[28].prix, stock[28].conditionnement, stock[28].adresse_image, stock[28].visibility)

# # .cacher()
# print(".cacher()", lol.cacher())

# # test fonction importer
# print(stock[1].id, stock[1].name, stock[1].description, stock[1].quantite, stock[1].prix, stock[1].conditionnement, stock[1].adresse_image, stock[1].visibility)
