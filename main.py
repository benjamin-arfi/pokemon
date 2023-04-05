from Types import *
from combat import *

input("demarer le jeu")
print("presentation de mes pokemon")
bulbizare = Type("bulbizare","feu","electrique")
bulbizare.afficher_pokemon()
salameche = Type("salameche", "terre","normal")
salameche.afficher_pokemon()
roucoul = Type("roucoul", "volant","feu")
roucoul.afficher_pokemon()
Carapuce = Type("carapuce", "eau","volant")
Carapuce.afficher_pokemon()
#mom pokemon choisi le type qui l'avantage le plus au niveau du point d'attaque et prends ce type 
chenipan = Type("chenipan", "fight","poisson")
chenipan.afficher_pokemon()
pikachu = Type("pikachu", "electrique","fight")
pikachu.afficher_pokemon()
feunard = Type("feunard", "glace","eau")
feunard.afficher_pokemon()

print("pour lancer le combat entre carapuce et salameche  lancer le combat appuyez sur enter ")

combat =input("lancer le combat")
combat = Combat(Carapuce, salameche)
combat.combat()

print("pour lancer le combat  entre pikachu et carapuce appuyez sur enter ")
combat =input("lancer le combat")
combat2 = Combat(pikachu, Carapuce)
combat2.combat() 


