# -*- coding: utf-8 -*-

# Import des différents fichiers et modules :
from classes.class_stock import stock 
from classes.class_panier import Panier, stockage_panier
from tkinter import *
from PIL import ImageTk, Image


class app_affichage_article:
    def __init__(self, root, identifiant):
        self.root = root
        self.root.geometry('900x600')
        self.root.title(stock[identifiant].getName())

        self.label = Label(root, text=stock[identifiant].getName())
        self.label.pack()

        #Gestion des frames
        root['bg']='white'

        # frame 1 ( page)
        self.Frame1 = Frame(root, borderwidth=2, relief=GROOVE)
        #Bouton
        self.acheter = Button(self.Frame1, text ='Ajoutez au panier', command = lambda: self.add_to_cart(identifiant))
        self.acheter.pack(side=BOTTOM, padx=5, pady=5)
        self.Frame1.pack(side=LEFT, padx=10, pady=10)
        
        # frame 2 ( image du produit )
        self.Frame2 = Frame(self.Frame1, borderwidth=2, relief=GROOVE)
        self.Frame2.pack(side=LEFT, padx=10, pady=10)
        #image

        # Read the Image
        # self.image = Image.open("./tomate.jpg")
        
        # # Resize the image using resize() method
        # self.resize_image = self.image.resize((200,200))
        # self.img = ImageTk.PhotoImage(self.resize_image)
        # self.label1 = Label(image=self.img)
        # self.label1.image = self.img
        # self.label = Label(self.Frame2, image = self.img)
        # self.label.pack()
        
        # frame 3 ( description du produit )        
        self.Frame3 = Frame(self.Frame1, borderwidth=2, relief=GROOVE)
        self.Frame3.pack(side=RIGHT and BOTTOM, padx=10, pady=10)
        
        # frame 4 ( Prix )
        
        self.Frame4 = Frame(self.Frame1, borderwidth=2, relief=GROOVE)
        self.Frame4.pack(side=RIGHT and BOTTOM, padx=10, pady=10)
        
        # frame 5 ( Quantite restante )
        self.Frame5 = Frame(self.Frame1, borderwidth=2, relief=GROOVE)
        self.Frame5.pack(side=RIGHT, padx=10, pady=10)
        
        #Applications des frames 
        Label(self.Frame1, text= "").pack(ipadx=100, ipady=200)
        Label(self.Frame2, text= "").pack(padx=100, pady=100)
        Label(self.Frame3, text= f"Prix unitaire : {stock[identifiant].getPrix()} €").pack(padx=10, pady=10)
        Label(self.Frame4, text= f"Quantité restante : {stock[identifiant].getQuantite()} articles en stock").pack(padx=10, pady=10)
        Label(self.Frame5, text= stock[identifiant].getDescription()).pack(padx=10, pady=10)


    def add_to_cart(self, identifiant):
        idstock = stock[identifiant].getId()
        name = stock[identifiant].getName()
        price = stock[identifiant].getPrix()

        if len(stockage_panier) <= 0 :
            obj = Panier(0, [[idstock, price, 1]])
            stockage_panier.append(obj)
            print(f"{name} ajouté au panier. Le panier contient : {obj.dico()}")
        else :
            stockage_panier[0].ajout([idstock, price, 1])
            print(f"{name} ajouté au panier. Le panier contient : {stockage_panier[0].dico()}")



def affichage_article(identifiant):
    root = Tk()
    app_affichage_article(root, identifiant)
    root.mainloop()

if __name__ == "__main__":
    affichage_article(identifiant)