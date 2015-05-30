from socapp.models.animal.model import Animal


class Cat(Animal):

    def __init__(self):
        Animal.__init__(self)
        self.hates_dogs = None

    def setName(self, name):
        Animal.setName(self, name)
        Animal.setSpecies(self, "Cat")

    def setHatesDogs(self, hates_dogs):
        self.hates_dogs = hates_dogs

    def getHatesDogs(self):
        return self.hates_dogs
