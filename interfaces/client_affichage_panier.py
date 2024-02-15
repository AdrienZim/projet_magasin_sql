# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
from classes.class_panier import stockage_panier

class PanierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Panier en ligne")
        self.root.geometry("900x600")

        # Variables pour stocker les éléments du panier
        # self.panier_items = stockage_panier

        # Widgets
        self.label = tk.Label(root, text="Votre Panier:")
        self.label.pack(pady=10)

        self.listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.listbox.pack(pady=10)

        self.ajouter_button = tk.Button(root, text="Valider le panier", command=self.valider_le_panier)
        self.ajouter_button.pack(pady=5)

        self.vider_button = tk.Button(root, text="Vider le panier", command=lambda: self.vider_panier(self.panier_items))
        self.vider_button.pack(pady=5)

    def valider_le_panier(self):
        messagebox.showinfo("Validation", "Le panier a été validé.")

    def vider_panier(self, panier):
        del panier[0]
        messagebox.showinfo("Panier vide", "Le panier a été vidé.")
        self.root.destroy()

def main_panier():
    root = tk.Tk()
    PanierApp(root)
    root.mainloop()

if __name__ == "__main__":
    main_panier()