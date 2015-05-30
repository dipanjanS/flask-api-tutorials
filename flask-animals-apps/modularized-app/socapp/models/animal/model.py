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
