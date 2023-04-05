import tkinter as tk
from Types import *
from combatgui import *
from pokemon import *
class PokemonGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sélectionnez votre Pokémon")

        # Créer les widgets pour la sélection de Pokémon
        self.label = tk.Label(master, text="Choisissez votre Pokémon :")
        self.label.grid(row=0, column=0)

        self.pokemon_list = [
            Type("bulbizare","feu","electrique"),
            Type("salameche", "terre","normal"),
            Type("roucoul", "volant","feu"),
            Type("pikachu", "electrique","fight"),
        ]

        self.var = tk.StringVar()
        self.var.set(self.pokemon_list[0].get_nom())

        self.option_menu = tk.OptionMenu(master, self.var, *[p.get_nom() for p in self.pokemon_list])
        self.option_menu.grid(row=0, column=1)

        self.button = tk.Button(master, text="Démarrer le combat", command=self.start_combat)
        self.button.grid(row=1, column=0, columnspan=2)

    def start_combat(self):
        selected_pokemon = None
        for p in self.pokemon_list:
            if p.get_nom() == self.var.get():
                selected_pokemon = p
                break

        if selected_pokemon is None:
            return

        # Fermer la fenêtre de sélection de Pokémon
        self.master.destroy()

        # Démarrer le combat
        root = tk.Tk()
        combat_gui = CombatGUI(root, selected_pokemon,Type("feunard", "glace","eau") )
        root.mainloop()
