# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 09:16:59 2024

@author: douchinap

"""
import csv
from fonctions import sql_execute, sql_execute_select

# SOUS LA FORME {num_panier:[num_client,[[num_article,prix,quantitÈ],[num_article,prix,quantitÈ]],total]}
# panier = {69:[2,[[5,2,3],[2,4,6]]]}

stockage_panier = []

def prix_total(panier,num_panier):
    total = 0
    for e in panier[num_panier][1] :
        total += e[1]*e[2]
    return total

class Panier():
    def __init__(self,num_client,contenu):
        # Recherche du numéro de panier
        sql_request = """
            UPDATE parametre
            SET    'valeur' = valeur + 1 
            WHERE  nom = 'Dernier_num_panier'
        ;"""
        # assert sql_execute(sql_request) == True, "L'enregistrement du numéro de panier a échoué."
        sql_execute(sql_request)

        sql_select = """
            SELECT  valeur
            FROM    parametre
            WHERE   nom = 'Dernier_num_panier'
        ;"""
        num_panier_ext = sql_execute_select(sql_select)
        print(num_panier_ext)
        
        self.num_panier = num_panier_ext
        self.num_client = num_client
        self.contenu = contenu

    def dico(self):
        P = {self.num_panier:[self.num_client,self.contenu]}
        P[self.num_panier].append(prix_total(P, self.num_panier))
        return P
    
    def ajout(self,nouvel_article):
        P = self.dico()
        P[self.num_panier][1].append(nouvel_article)
        t = prix_total(self.dico(), self.num_panier)
        P[self.num_panier][-1] = t
        return P
        
    def suppr(self,n):
        P = self.dico()
        del P[self.num_panier][1][n-1]
        t = prix_total(self.dico(), self.num_panier)
        P[self.num_panier][-1] = t
        assert n < len(P[self.num_panier][1])
        return P


###################################################################
######################### Tests unitaires #########################
###################################################################

# panier = Panier(2,[[5,2,3],[2,4,6]])
# print(panier.ajout([6,99,2]))
# print(panier.suppr(1))