from pokemon import*

class Type(Pokemon):

    def __init__(self,nom,tipes):
        
        self.types = {"feu":{ "point_de_vie":13 , "niveau": 1 , "defense": 1 , "puissance_attaque": 2,"fort":"terre","faible":"eau","fortd":"eau","faibled":"terre" },
                        "eau":{"point_de_vie": 10 , "niveau": 9 , "defense": 7 , "puissance_attaque": 2,"fort":"feu","faible":"terre","fortd":"terre","faibled":"feu"},
                        "terre":{"point_de_vie": 10 , "niveau" : 2, "defense": 2 , "puissance_attaque": 3,"fort":"eau","faible":"feu","fortd":"feu","faibled":"eau"},
                        "normal":{"point_de_vie": 10 , "niveau": 0 , "defense": 0 , "puissance_attaque": 0}}
        self.tipe = tipes
        self.fort = self.types[tipes]["fort"]
        self.faible = self.types[tipes]["faible"]
        self.defense =  self.types[tipes]["defense"]
        self.attaque = self.types[tipes]["puissance_attaque"]
        

        Pokemon.__init__(self, nom, self.types[tipes]["point_de_vie"], self.types[tipes]["niveau"], self.types[tipes]["puissance_attaque"], self.types[tipes]["defense"])
    
    def get_typespo(self):
        return(self.tipe)
    
    def get_puissance_attaquepo(self):
        return (self.attaque)
    
    def get_fort(self):
        return(self.fort)
    
    def get_faible(self):
        return(self.faible)

    def get_defensepo(self):
        return(self.defense)