from Types import *
from combat import *

bulbizare = Type("bulbizare","feu")
bulbizare.afficher_pokemon()
salameche = Type("salameche", "terre")
salameche.afficher_pokemon()

combat = Combat(bulbizare, salameche)
combat.combat()
