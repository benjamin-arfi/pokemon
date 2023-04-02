"""class Normal(Pokemon):
    def __init__(self, nom, niveau=1):
        super().__init__(nom, niveau)
        self.type = "Normal"
        self.point_de_vie = 100 + (10 * niveau)
        self.puissance_attaque = 10 + (2 * niveau)
        self.defense = 5 + niveau

class Feu(Pokemon):
    def __init__(self, nom, niveau=1):
        super().__init__(nom, niveau)
        self.type = "Feu"
        self.point_de_vie = 100 + (8 * niveau)
        self.puissance_attaque = 12 + (3 * niveau)
        self.defense = 3 + niveau

    def get_attack_effectiveness(self, other):
        effectiveness = 1
        if other.type_ == "Plante":
            effectiveness = 2
        elif other.type_ == "Eau":
            effectiveness = 0.5
        return effectivenes


class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def get_typeAdversaire(self):

        self.attaquant = self.pokemon1
        self.adversaire = self.pokemon2

        if  self.attaquant.get_fort() == self.adversaire.get_typespo() :
            print(self.adversaire.get_typespo())
            print(self.adversaire.get_point_de_viepo() - (self.attaquant.get_puissance_attaquepo()*2 - self.adversaire.get_defensepo()))
            return self.adversaire.get_point_de_viepo() - (self.attaquant.get_puissance_attaquepo()*2 - self.adversaire.get_defensepo())
        elif self.attaquant.get_faible() == self.adversaire.get_typespo():
            return (self.attaquant.get_puissance_attaquepo()*0.5  - self.adversaire.get_defensepo())-self.adversaire.get_point_de_viepo()
        else:
            return (self.attaquant.get_puissance_attaquepo()*1 - self.adversaire.get_defensepo())-self.adversaire.get_point_de_viepo()


    def est_fini(self):
        print('test')
        return self.get_typeAdversaire() <= 0
        

    def get_vainqueur(self):
        if self.get_typeAdversaire() > 0:
            return self.attaquant.get_nom()
        

    def combat(self):
        print("Le combat commence !")
        tour = 1
        while not self.est_fini():
            print(f"Tour {tour}")
            print(f"{self.pokemon1.get_nom()}")
            print(f"{self.pokemon2.get_nom()} ")
            
            if tour % 2 == 1:
                self.attaquant = self.pokemon1
                self.adversaire = self.pokemon2
                print(self.get_typeAdversaire())
                tour +=1
            else:
                self.attaquant = self.pokemon2
                self.adversaire = self.pokemon1
                tour +=1
            print(f"{self.attaquant.get_nom()} attaque !")
            
            
        print(f"{self.get_vainqueur()} a gagné le combat !")
        print(f"{self.pokemon1.get_nom()} ")
        print(f"{self.pokemon2.get_nom()} ")


from Types import *
from combat import *

bulbizare = Type("bulbizare","feu")
bulbizare.afficher_pokemon()
salameche = Type("salameche", "terre")
salameche.afficher_pokemon()

combat = Combat(bulbizare, salameche)
combat.combat()
"""