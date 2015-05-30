from socapp.models.animal.model import Animal

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        self.chases_cats = None

    def setName(self, name):
        Animal.setName(self, name)
        Animal.setSpecies(self, "Dog")

    def setChasesCats(self, chases_cats):
        self.chases_cats = chases_cats

    def getChasesCats(self):
        return self.chases_cats
