class Kissa:
    count : int = 0
    def __init__(self, name : str,  byear: int, breed : str= "tuntematon"):
        self.name :str= name
        self.breed :str= breed
        self.byear :int= byear
        Kissa.count += 1


kissa: Kissa = Kissa("Pörri","Calico",1997)
kissa2: Kissa = Kissa("Rölli",1997)
print(kissa.name)
print(kissa2.name,kissa2.breed,kissa2.byear)
print(Kissa.count)
