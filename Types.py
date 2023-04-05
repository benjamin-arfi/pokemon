from pokemon import*

class Type(Pokemon):

    def __init__(self,nom,tipes,tipes2):
        
        self.types = {"feu":{ "point_de_vie":13 , "niveau": 1 , "defense": 3 , "puissance_attaque": 5,"fort":"terre","faible":"eau" },
                        "eau":{"point_de_vie": 15 , "niveau": 9 , "defense": 2 , "puissance_attaque": 9,"fort":"feu","faible":"terre"},
                        "terre":{"point_de_vie": 12 , "niveau" : 2, "defense": 2, "puissance_attaque": 8,"fort":"eau","faible":"feu"},
                        "normal":{"point_de_vie": 10 , "niveau": 0 , "defense": 0 , "puissance_attaque": 4,"fort":"eau","faible":"feu"},
                        "electrique":{ "point_de_vie":14 , "niveau": 1 , "defense": 4 , "puissance_attaque": 8,"fort":"terre","faible":"eau"},
                        "glace":{ "point_de_vie":17 , "niveau": 1 , "defense": 3 , "puissance_attaque": 10,"fort":"electrique","faible":"feu"},
                        "fight":{ "point_de_vie":13 , "niveau": 1 , "defense": 3 , "puissance_attaque": 9,"fort":"glace","faible":"electrique"},
                        "poisson":{ "point_de_vie":11 , "niveau": 1 , "defense": 3 , "puissance_attaque": 8,"fort":"terre","faible":"eau"},
                        "plante": { "point_de_vie":10 , "niveau": 1 , "defense": 2 , "puissance_attaque": 7,"fort":"terre","faible":"eau"},
                        "volant":{ "point_de_vie":17 , "niveau": 1 , "defense": 4 , "puissance_attaque": 3,"fort":"eau","faible":"glace"}
                        }

        self.tipe = tipes
        self.tipe2 = tipes2
        self.fort = self.types[tipes]["fort"]
        self.faible = self.types[tipes]["faible"]
        self.defense =  self.types[tipes]["defense"]
        self.attaque = self.types[tipes]["puissance_attaque"]
        self.vie = self.types[tipes]["point_de_vie"]
        self.attaque2 = self.types[tipes2]["puissance_attaque"]
        self.defense2 =  self.types[tipes2]["defense"]
        self.faible2 = self.types[tipes2]["faible"]
        self.fort2 = self.types[tipes2]["fort"]
        self.vie2 = self.types[tipes2]["point_de_vie"]
        if self.attaque2 > self.attaque:
            return(Pokemon.__init__(self, nom, self.types[tipes2]["point_de_vie"], self.types[tipes2]["niveau"], self.types[tipes2]["puissance_attaque"], self.types[tipes2]["defense"]))
        else:
            return(Pokemon.__init__(self, nom, self.types[tipes]["point_de_vie"], self.types[tipes]["niveau"], self.types[tipes]["puissance_attaque"], self.types[tipes]["defense"]))
        
    
    def get_typespo(self):
        if self.attaque2 > self.attaque:
            return(self.tipe2)
        else:
            return(self.types)
    
    def get_puissance_attaquepo(self):
        if self.attaque2 > self.attaque:
            return (self.attaque2)
        else:
            return(self.attaque)
       
    
    def get_fort(self):
        if self.attaque2 > self.attaque:
            return (self.fort2)
        else:
            return(self.fort)
    
    def get_faible(self):
        if self.attaque2 > self.attaque:
            return (self.faible2)
        else:
            return(self.faible)

    def get_defensepo(self):
        if self.attaque2 > self.attaque:
            return (self.defense2)
        else:
            return(self.defense)

   