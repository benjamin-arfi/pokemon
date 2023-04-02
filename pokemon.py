class Pokemon:
    def __init__(self,nom,point_de_vie,niveau,puissance_attaque,defense):
        self.__nom = nom
        self.__point_de_vie = point_de_vie
        self.__niveau = niveau
        self.__puissance_attaque = puissance_attaque
        self.__defense = defense
        
        
    def get_nom(self):
        return self.__nom
    def set_nom(self,nom):
        self.__nom = nom
        return self.__nom
    def get_point_de_vie(self):
        return self.__point_de_vie
    def set_point_de_vie(self,point_de_vie):
        self.__point_de_vie = point_de_vie
    def get_niveau(self):
        return self.__niveau
    def get_puissance_attaque(self):
        return int(self.__puissance_attaque)
    def get_defense(self):
        return self.__defense
    def afficher_pokemon(self):
        print(f"(nom : {self.get_nom()}, vies : {self.get_point_de_vie()}, défense : {self.get_defense()}, attaque : {self.get_puissance_attaque()}).")



