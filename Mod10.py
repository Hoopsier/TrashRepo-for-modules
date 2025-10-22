class Kone():
    def tankaa():
        pass
### NOTE: Why the hell does type annotation not do shit? Like screw you python creator! 
class Boeing(Kone):
    bensaMax : int = 2000
    def __init__(self,vuosi:int,bensa:int,nimi:str):
        self.nimi = nimi
        self.vuosi :int= vuosi
        self.bensa :int = bensa
    def tankaa(self):
        self.bensa = self.bensaMax 

class TurkishAirline(Kone):
    bensaMax : int = 4000
    def __init__(self, vuosi:int, bensa:int,nimi:str):
        self.nimi = nimi
        self.vuosi :int= vuosi
        self.bensa :int = bensa
    def tankaa(self):
        self.bensa = self.bensaMax 
        

class Kentta():
    def __init__(self,nimi):
        self.nimi = nimi
        self.koneet = []
    def addKone(self, kone :Kone):
        self.koneet.append(kone)
    def haeKoneet(self):
        for kone in self.koneet:
            print(f"{kone.nimi}: {kone.bensa} of gas")
    def tankkaaKaikki(self):
        for kone in self.koneet:
            kone.tankaa()

kone1 = Boeing(1984,100,"Trash Heap")
kone2 = Boeing(1997,400, "Trash Heap 2.0")
kone3 = TurkishAirline(1987,2000, "Normal Plane")
kentta= Kentta("Smallest Airport")
kentta.addKone(kone1)
kentta.addKone(kone2)
kentta.addKone(kone3)
kentta.haeKoneet()
kentta.tankkaaKaikki()
kentta.haeKoneet()
