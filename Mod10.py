class Elain():
    def pet():
        pass

class Koira(Elain):
    def __init__(self,vuosi:int,nimi:str,haukku:str = "Vuh Vuh!"):
        self.nimi :str=nimi
        self.vuosi :int= vuosi
        self.haukku :str = haukku
    def pet(self):
        print(self.haukku)

class Kissa(Elain):
    def __init__(self, vuosi:int,nimi:str, purina:str = "pur"):
        self.nimi :str=nimi
        self.vuosi :int= vuosi
        self.purina :str= purina
    def pet(self):
        print(self.purina)
        

class Hoitola():
    def __init__(self):
        self.elaimet = []
    def addElain(self, elain :Elain):
        self.elaimet.append(elain)
    def getElaimet(self):
        for elain in self.elaimet:
            print(elain.nimi)
    def petElaimet(self):
        for elain in self.elaimet:
            elain.pet()

koira1 = Koira(1984,"Murre" )
koira2 = Koira(1997,"Musti" )
kissa1 = Kissa(1987,"Miuku")
htola = Hoitola()
htola.addElain(koira1)
htola.addElain(koira2)
htola.addElain(kissa1)
htola.getElaimet()
htola.petElaimet()
