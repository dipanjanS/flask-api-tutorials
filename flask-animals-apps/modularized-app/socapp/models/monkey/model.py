from socapp.models.animal.model import Animal

class Monkey(Animal):

    def __init__(self):
        Animal.__init__(self)
        self.eats_bananas = None

    def setName(self, name):
        Animal.setName(self, name)
        Animal.setSpecies(self, "Monkey")

    def setEatsBananas(self, eats_bananas):
        self.eats_bananas = eats_bananas

    def getEatsBananas(self):
        return self.eats_bananas
