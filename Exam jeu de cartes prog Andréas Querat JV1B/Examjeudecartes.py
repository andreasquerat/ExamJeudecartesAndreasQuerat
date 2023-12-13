class Cartes :
    def __init__(self, nom, couts, description):
        self.__nom = nom
        self.__couts = couts
        self.__description = description
    def getNom(self):
        return self.__nom
    def getCouts(self):
        return self.__couts
    def getDescription(self):
        return self.__description
    
class Mage :
    def __init__(self,nom,hp,actualmana, totalmana) : 
        self.__nom = nom
        self.__hp = 30
        self.__actualmana = actualmana
        self.__totalmana = 10
        self.hand = []
        self.discard_pile = []
        self.play_area = [] 
    
    def cartesajouer(self,cartes):
       if cartes.mana_cost <= self.actual_mana_points and cartes in self.hand:
          self.hand.remove(cartes)
          self.play_area.append(cartes)
          self.actual_mana_points -= cartes.mana_cost 
       else:
           print("Pas assez de mana pour jouer ou vous n'avez pas la carte.")

    def recuperermana(self):
        self.actual_mana_points = self.total_mana_points
    
    def attack(self, target, creature):
         if creature in self.play_area:
            target.take_damage(creature.attack_points)
         else:
            print("Votre créature n'est pas sur le champs de bataille.")

    def take_damage(self, damage):
         self.health_points -= damage
         if self.health_points <= 0:
            self.health_points = 0
            print("Votre ennemeni a été vaincu !")

class Cristal(Cartes) :
    def __init__(self, valeur, cout_mana):
        self.valeur = valeur
    def jouer (self, jouer):
        jouer.zone_de_jeu.ajouter(self)
        jouer.mana_max += self.valeur

class Creatures(Cartes) :
    def __init__(self, coutmana, healthpoint, scoreAtk):
