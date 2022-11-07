
class Junction():

    def __init__(self, id: int):
        self._id = id
        self._neighbouringJunctions = []
        self._trafficLightsInJunction = []


    def __repr__(self):
        return f"Id: {self._id}"

    
    #methods for creating and removing junction neighbour pairs
    #possibly add limit to number of Junctions in NeighbouringJunctions (logically cannot be more than 4)
    def addJunctionNeighbourPair(self, neighbouringJunctionToAdd: "Junction"):
        try:
            if not isinstance(neighbouringJunctionToAdd, Junction):
                raise TypeError

            if neighbouringJunctionToAdd not in self._neighbouringJunctions:
                self._neighbouringJunctions.append(neighbouringJunctionToAdd)
                #calls the method again on the neighbouringJunctionToAdd object, using the current object as input
                #a loop is avoided as once the neighbouringJunctionToAdd object calls the method again, the Junctions are in the list and this block of code is skipped.
                neighbouringJunctionToAdd.addJunctionNeighbourPair(self)

        except TypeError:
            print("TypeError: Input to addJunctionNeighbourPair method must be an instance of Junction class")
        return

    def removeJunctionNeighbourPair(self, neighbouringJunctionToRemove: "Junction"):
        pass

    def getNeighbouringJunctions(self):
        return self._neighbouringJunctions



def testJunctionPairMethods():
    #Attempt to run the addJunctionNeighbourPair method with invalid input, should raise TypeError
    print("Running addNeighbourPair() method with an input of 17...") 
    J1.addJunctionNeighbourPair(17)

    #print J1s neighbouringJunctions (empty)
    print(f"{J1} NeighbourList: {J1.getNeighbouringJunctions()}")


    #Attempt to run the addJunctionNeighbourPair method successfully
    print("Adding (J1, J2), (J1, J3), (J2, J4), (J3, J4) as neighbour pairs...")
    J1.addJunctionNeighbourPair(J2)
    J1.addJunctionNeighbourPair(J3)
    J2.addJunctionNeighbourPair(J4)
    J3.addJunctionNeighbourPair(J4)

    #print neighbouringJunctions of all Junctions
    print(f"{J1} NeighbourList: {J1.getNeighbouringJunctions()}")
    print(f"{J2} NeighbourList: {J2.getNeighbouringJunctions()}")
    print(f"{J3} NeighbourList: {J3.getNeighbouringJunctions()}")
    print(f"{J4} NeighbourList: {J4.getNeighbouringJunctions()}")



if __name__ == "__main__":
    J1= Junction(1)
    J2 = Junction(2)
    J3 = Junction(3)
    J4 = Junction(4)

    print("Testing Junction addNeighbourPair and removeNeighbourPair methods...")
    testJunctionPairMethods()



