from pokemon import *
from Types import *

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def est_fini(self):
        if self.Viepo1() <= 0 or self.Viepo2() <= 0:
            return True
        else:
            return False

    def combat(self):

        print("Le combat commence !")
        while not self.est_fini():
            print(f"{self.pokemon2.get_nom()} attaque !")
            dommage2 = self.attaque_pokemon2()
            self.pokemon1.set_point_de_vie(self.pokemon1.get_point_de_vie() - dommage2)
            print(f"{self.pokemon1.get_nom()} a subi {dommage2} points de dégâts.")
            print(f"{self.Viepo1()} points de vie restants pour {self.pokemon1.get_nom()}.")

            if self.est_fini():
                break

            print(f"{self.pokemon1.get_nom()} attaque !")
            dommage1 = self.attaque_pokemon1()
            self.pokemon2.set_point_de_vie(self.pokemon2.get_point_de_vie() - dommage1)
            print(f"{self.pokemon2.get_nom()} a subi {dommage1} points de dégâts.")
            print(f"{self.Viepo2()} points de vie restants pour {self.pokemon2.get_nom()}.")

        print(f"{self.get_vainqueur()} a gagné le combat !")
        print(f"{self.get_vainqueur()} a maintenant {self.gagner_niveau()} de point de vie" )
    def get_vainqueur(self):
        if self.Viepo1() > 0 and self.Viepo2() <= 0:
            return self.pokemon1.get_nom() 
        elif self.Viepo2() > 0 and self.Viepo1() <= 0:
            return self.pokemon2.get_nom() 
        else:
            return "Match nul !"
    def set_attaque(self,attaque):
        self.attaque = attaque
    def gagner_niveau(self):
        if self.Viepo1() > 0 and self.Viepo2() <= 0:
           self.set_attaque(self.pokemon1.get_puissance_attaquepo() + 2)
           return self.pokemon1.get_puissance_attaquepo()
        else:
           self.set_attaque(self.pokemon2.get_puissance_attaquepo() + 2)
           return self.pokemon2.get_puissance_attaquepo()
        
    def attaque_pokemon2(self):
        if  self.pokemon2.get_fort() == self.pokemon1.get_typespo() :
            return ( self.pokemon2.get_puissance_attaque()*2 - self.pokemon1.get_defensepo())
        elif self.pokemon2.get_faible() == self.pokemon1.get_typespo(): 
            return ( self.pokemon2.get_puissance_attaque()*0.5 - self.pokemon1.get_defensepo())
        elif self.pokemon2.get_typespo() != "normal" and self.pokemon1.get_typespo() == "normal":
            return(self.pokemon2.get_puissance_attaque()*0.75 - self.pokemon1.get_defensepo())
        else:
            return( self.pokemon2.get_puissance_attaque()*1 - self.pokemon1.get_defensepo())

        

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
    
    def Viepo1(self):
        return self.pokemon1.get_point_de_vie()
