
class Junction():

    def __init__(self, id: int) -> None:
        self._id = id
        self._neighbouringJunctions = []
        self._trafficLightsInJunction = []


    def __repr__(self) -> str:
        return f"Junction id: {self._id}"

    
    #methods for creating, removing, and viewing junction neighbour pairs
    #possibly add limit to number of Junctions in NeighbouringJunctions (logically cannot be more than 4)
    def addJunctionNeighbourPair(self, neighbouringJunctionToAdd: "Junction") -> None:
        try:
            if not isinstance(neighbouringJunctionToAdd, Junction):
                raise TypeError

            if neighbouringJunctionToAdd not in self._neighbouringJunctions:
                self._neighbouringJunctions.append(neighbouringJunctionToAdd)
                #calls the method again on the neighbouringJunctionToAdd object, using the current object as input
                #a loop is avoided as once the neighbouringJunctionToAdd object calls the method again, the Junctions are in the list and this block of code is skipped.
                print(f"Successfully added {neighbouringJunctionToAdd} to {self}")
                neighbouringJunctionToAdd.addJunctionNeighbourPair(self)

        except TypeError:
            print("TypeError: Input to addJunctionNeighbourPair method must be an instance of Junction class")
        return

    def removeJunctionNeighbourPair(self, neighbouringJunctionToRemove: "Junction") ->None:
        try:
            if not isinstance(neighbouringJunctionToRemove, Junction):
                raise TypeError

            if neighbouringJunctionToRemove in self._neighbouringJunctions:  
                self._neighbouringJunctions.remove(neighbouringJunctionToRemove)
                print(f"Successfully removed {neighbouringJunctionToRemove} from {self}")
                neighbouringJunctionToRemove._neighbouringJunctions.remove(self)

        except TypeError:
            print("TypeError: Input to removeJunctionNeighbourPair method must be an instance of Junction class")
        return

    def getNeighbouringJunctions(self) -> list:
        return self._neighbouringJunctions

    
    #methods for adding and removing traffic lights to junctions trafficLightsInJunction list
    def addTrafficLight(self, trafficLightToAdd) -> None:
        pass

    def removeTrafficLight(self, trafficLightToRemove) -> None:
        pass

    #get list of traffic lights in junction
    def getTrafficLights(self) -> list:
        return self._trafficLightsInJunction



def testJunctionPairMethods():
    print("Testing junctionNeighbourPair addition and removal methods...")
    print("\n\n")

    #Attempt to run the addJunctionNeighbourPair method with invalid input, should raise TypeError
    print("Running addNeighbourPair() method with an input of 17...") 
    testJunction1 .addJunctionNeighbourPair(17)

    #print testJunction1 s neighbouringJunctions (empty)
    print(f"{testJunction1 } NeighbourList: {testJunction1 .getNeighbouringJunctions()}")
    print("\n")

    #Attempt to run the addJunctionNeighbourPair method successfully
    print("Adding (testJunction1 ,  testJunction2), (testJunction1 , testJunction3),  testJunction2, testJunction4), (testJunction3, testJunction4) as neighbour pairs...")
    testJunction1 .addJunctionNeighbourPair(testJunction2)
    testJunction1 .addJunctionNeighbourPair(testJunction3)
    testJunction2.addJunctionNeighbourPair(testJunction4)
    testJunction3.addJunctionNeighbourPair(testJunction4)
    print("\n")

    #print neighbouringJunctions of all Junctions
    print("Printing neighbouringJunctions of all Junctions...")
    print(f"{testJunction1 }, NeighbourList: {testJunction1 .getNeighbouringJunctions()}")  #2, 3
    print(f"{testJunction2}, NeighbourList:   {testJunction2.getNeighbouringJunctions()}")  #1, 4
    print(f"{testJunction3}, NeighbourList: {testJunction3.getNeighbouringJunctions()}")  #1, 4
    print(f"{testJunction4}, NeighbourList: {testJunction4.getNeighbouringJunctions()}")  #2, 3
    print("\n")


    #test removeJunctionNeighbourPair with invalid input
    print("Running removeJunctionNeighbourPair with an input of \"junction 2\"...")
    testJunction1 .removeJunctionNeighbourPair("junction 2")    #TypeError
    print(f"{testJunction1}, NeighbourList: {testJunction1 .getNeighbouringJunctions()}")
    print("\n")

    #test removeJunctionNeighbourPair with Junction not in neighbouringJunctions
    print(f"Removing {testJunction1} and {testJunction4} neighbour pair...")
    print(f"Before: {testJunction1}, NeighbourList: {testJunction1.getNeighbouringJunctions()}")
    testJunction1.removeJunctionNeighbourPair(testJunction4)
    print(f"After: {testJunction1}, NeighbourList: {testJunction1.getNeighbouringJunctions()}")
    print("\n")

    #test removeJunctionNeighbourPair successfully
    print(f"Removing {testJunction1} and {testJunction2} neighbour pair...")
    testJunction2.removeJunctionNeighbourPair(testJunction1)
    print(f"{testJunction1}, NeighbourList: {testJunction1 .getNeighbouringJunctions()}")   #3
    print(f"{testJunction2}, NeighbourList:   {testJunction2.getNeighbouringJunctions()}")  #4
    print("\n")

    print("Testing of junctionNeighbourPair methods complete")


    


if __name__ == "__main__":
    testJunction1 = Junction(1)
    testJunction2 = Junction(2)
    testJunction3 = Junction(3)
    testJunction4 = Junction(4)

    print("Testing Junction addNeighbourPair and removeNeighbourPair methods...")
    testJunctionPairMethods()



