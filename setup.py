from junction import Junction
from light import Light

class Setup():

    def __init__(self) -> None:
        self.setupRoad()

    def setupRoad(self)  -> None:
        entryJunction1 = Junction(isEntryJunction=True)
        entryJunction2 = Junction(isEntryJunction=True)
        Junction1 = Junction()
        Junction2 = Junction()
        Junction3 = Junction()
        Junction4 = Junction()
        Junction1.addJunctionNeighbourPair(entryJunction1)
        Junction1.addJunctionNeighbourPair(Junction2)
        Junction1.addJunctionNeighbourPair(Junction4)
        Junction2.addJunctionNeighbourPair(Junction3)
        Junction3.addJunctionNeighbourPair(Junction4)
        Junction4.addJunctionNeighbourPair(entryJunction2)
        self.createLights()

    def createLights(self):
        
        return