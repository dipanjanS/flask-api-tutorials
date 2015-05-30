class Animal:

    def __init__(self):
        self.name = None
        self.species = None

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setSpecies(self, species):
        self.species = species

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)


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
