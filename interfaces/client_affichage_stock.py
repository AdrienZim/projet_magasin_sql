# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 08:11:30 2024

@author: michelra
"""

# Import des modules
import tkinter as tk
from tkinter import ttk

# Import des différents fichiers :
from classes.class_stock import stock, search_num_article
from interfaces.client_affichage_article import affichage_article
from interfaces.client_affichage_panier import main_panier

class StockApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('900x600')
        self.root.title("Stock disponible")

        # Données du stock
        self.stock_data = []
        for element in stock:
            if stock[element].getVisibility() == True :
                self.stock_data.append((stock[element].getName(), stock[element].getDescription(), stock[element].getQuantite(), f"{stock[element].getPrix()} €", stock[element].getConditionnement(), stock[element].getVisibility()))
        
        # Créez un Treeview pour afficher le stock
        self.tree = ttk.Treeview(root, columns=("Produit", "Description", "Quantité", "Prix", "Conditionnement"), show="headings")
        self.tree.heading("Produit", text="Produit", command=lambda: self.sort_column("Produit"))
        self.tree.heading("Description", text="Description")
        self.tree.heading("Quantité", text="Quantité")
        self.tree.heading("Prix", text="Prix")
        self.tree.heading("Conditionnement", text="Conditionnement")
        
        # Définition des tailles de certaines colonnes
        self.tree.column("Quantité", width=100)
        self.tree.column("Prix", width=100)
        self.tree.column("Conditionnement", width=120)
        
        # Remplissez le Treeview avec les données du stock
        self.update_stock()
        
        # Associez la fonction click_handler à l'événement de clic sur une ligne
        self.tree.bind("<ButtonRelease-1>", self.click_handler)

        # Utilisez et placez pack pour ajuster le Treeview à la fenêtre
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Ajoutez un bouton en dessous du Treeview
        self.button = tk.Button(root, text="Panier", command=self.ouverture_panier)
        self.button.pack(pady=10)

    def update_stock(self):
        # Effacez les données existantes dans le Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Ajoutez les données actuelles du stock dans le Treeview
        for data in self.stock_data:
            self.tree.insert("", "end", values=data)
    
    def click_handler(self, event):
        # Récupérez la région sur laquelle l'utilisateur a cliqué
        region = self.tree.identify_region(event.x, event.y)

        # Vérifiez si l'événement de clic provient d'une colonne
        if region == "heading":
            return  # Ne faites rien si le clic provient d'une colonne

        # Récupérez l'élément sélectionné dans le Treeview
        item = self.tree.selection()

        # Vérifiez s'il y a une sélection
        if item:
            # Affichage du détails de l'article et Récupération des valeurs de la ligne sélectionnée
            values = self.tree.item(item, "values")
            affichage_article(search_num_article(values[0]))
    
    def sort_column(self, column):
        # Obtenez les données actuelles du Treeview
        data = [(self.tree.set(child, column), child) for child in self.tree.get_children("")]

        # Triez les données en fonction de la colonne sélectionnée
        data.sort()

        for i, item in enumerate(data):
            # Reconfigurez les éléments du Treeview dans l'ordre trié
            self.tree.move(item[1], "", i)
            
    def ouverture_panier(self):
        main_panier()
        # Fonction associée au bouton pour envoyer un message dans la console
        # print("Message envoyé depuis le bouton. => Ouverture d'une fenêtre contenant le panier de ?")

def main_client():
    root = tk.Tk()
    StockApp(root)
    root.mainloop()

if __name__ == "__main__":
    main_client()
