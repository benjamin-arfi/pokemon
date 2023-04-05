import tkinter as tk
from Types import *
from combatgui import *
from pokemon import *
from slepok import*
root = tk.Tk()
root.title("Combat Pokémon")
fenetre = PokemonGUI(root)
root.destroy()
root.mainloop()

