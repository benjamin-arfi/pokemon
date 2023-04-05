import tkinter as tk
from pokemon import *
from Types import *

class CombatGUI:
    def __init__(self, master, pokemon1, pokemon2):
        self.master = master
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

        # Créer les widgets pour afficher les noms et les points de vie des deux Pokémons
        self.pokemon1_name = tk.Label(master, text=pokemon1.get_nom())
        self.pokemon1_name.grid(row=0, column=0)
        self.pokemon1_hp = tk.Label(master, text=f"HP: {pokemon1.get_point_de_vie()}")
        self.pokemon1_hp.grid(row=0, column=1)
        self.pokemon1_defense = tk.Label(master, text=f"defense: {pokemon1.get_defensepo()}")
        self.pokemon1_defense.grid(row=0, column=2)
        self.pokemon1_attaque = tk.Label(master, text=f"attaque: {pokemon1.get_puissance_attaquepo()}")
        self.pokemon1_attaque.grid(row=0, column=3)
        self.pokemon2_name = tk.Label(master, text=pokemon2.get_nom())
        self.pokemon2_name.grid(row=1, column=0)
        self.pokemon2_hp = tk.Label(master, text=f"HP: {pokemon2.get_point_de_vie()}")
        self.pokemon2_hp.grid(row=1, column=1)
        self.pokemon2_defense = tk.Label(master, text=f"defense: {pokemon2.get_defensepo()}")
        self.pokemon2_defense.grid(row=1, column=2)
        self.pokemon2_attaque = tk.Label(master, text=f"attaque: {pokemon2.get_puissance_attaquepo()}")
        self.pokemon2_attaque.grid(row=1, column=3)

        # Créer le bouton pour démarrer le combat
        self.start_button = tk.Button(master, text="Démarrer le combat", command=self.combat)
        self.start_button.grid(row=2, column=0)

        # Créer une zone de texte pour afficher les messages de combat
        self.text_box = tk.Text(master, height=10, width=50)
        self.text_box.grid(row=3, column=0, columnspan=2)

    def est_fini(self):
        if self.pokemon1.get_point_de_vie() <= 0 or self.pokemon2.get_point_de_vie() <= 0:
            return True
        else:
            return False

    def combat(self):
        self.text_box.insert(tk.END, "Le combat commence !\n")

        while not self.est_fini():
            self.text_box.insert(tk.END, f"{self.pokemon2.get_nom()} attaque !\n")
            dommage2 = self.attaque_pokemon2()
            self.pokemon1.set_point_de_vie(self.pokemon1.get_point_de_vie() - dommage2)
            self.pokemon1_hp.config(text=f"HP: {self.pokemon1.get_point_de_vie()}")
            self.text_box.insert(tk.END, f"{self.pokemon1.get_nom()} a subi {dommage2} points de dégâts.\n")
            self.text_box.insert(tk.END, f"{self.pokemon1.get_point_de_vie()} points de vie restants pour {self.pokemon1.get_nom()}.\n")

            if self.est_fini():
                break

            self.text_box.insert(tk.END, f"{self.pokemon1.get_nom()} attaque !\n")
            dommage1 = self.attaque_pokemon1()
            self.pokemon2.set_point_de_vie(self.pokemon2.get_point_de_vie() - dommage1)
            self.pokemon2_hp.config(text=f"HP: {self.pokemon2.get_point_de_vie()}")
            self.text_box.insert(tk.END, f"{self.pokemon2.get_nom()} a subi {dommage1} points de dégâts.\n")
            self.text_box.insert(tk.END, f"{self.pokemon2.get_point_de_vie()} points de vie restants pour {self.pokemon2.get_nom()}.\n")

        self.text_box.insert(tk.END, f"{self.get_vainqueur()} a gagner le combat \n")
    def Viepo1(self):
        return self.pokemon1.get_point_de_vie()

    def Viepo2(self):
        return self.pokemon2.get_point_de_vie()

    def attaque_pokemon1(self):
        if  self.pokemon1.get_fort() == self.pokemon2.get_typespo() :
            return self.pokemon1.get_puissance_attaque()*2 - self.pokemon2.get_defensepo()
        elif self.pokemon1.get_faible() == self.pokemon2.get_typespo(): 
            return self.pokemon1.get_puissance_attaque()*0.5 - self.pokemon2.get_defensepo()
        elif self.pokemon1.get_typespo() != "normal" and self.pokemon2.get_typespo() == "normal":
            return(self.pokemon1.get_puissance_attaque()*0.75 - self.pokemon2.get_defensepo())
        else:
            return self.pokemon1.get_puissance_attaque()*1 - self.pokemon2.get_defensepo()

    def attaque_pokemon2(self):
        if  self.pokemon2.get_fort() == self.pokemon1.get_typespo() :
            return ( self.pokemon2.get_puissance_attaque()*2 - self.pokemon1.get_defensepo())
        elif self.pokemon2.get_faible() == self.pokemon1.get_typespo(): 
            return ( self.pokemon2.get_puissance_attaque()*0.5 - self.pokemon1.get_defensepo())
        elif self.pokemon2.get_typespo() != "normal" and self.pokemon1.get_typespo() == "normal":
            return(self.pokemon2.get_puissance_attaque()*0.75 - self.pokemon1.get_defensepo())
        else:
            return( self.pokemon2.get_puissance_attaque()*1 - self.pokemon1.get_defensepo())

    def get_vainqueur(self):
        if self.Viepo1() > 0 and self.Viepo2() <= 0:
            return self.pokemon1.get_nom() 
        elif self.Viepo2() > 0 and self.Viepo1() <= 0:
            return self.pokemon2.get_nom() 
        else:
            return "Match nul !"

