class elain():
    species =""
    name =""
    def __init__(self, name,species):
        self.species=species
        self.name = name
    def printInfo(self):
        print(self.name, self.species)

class kissa(elain):
    def __init__(self, name,species, roams = True):
        super().__init__(name,species)
        self.roams = roams
    def printInfo(self):
        print(self.name, self.species, self.roams)

x = elain("a","b")
y = kissa("f","e")
z = kissa("c","d")

x.printInfo();
y.roams = False
y.printInfo();
z.printInfo();
