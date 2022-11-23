from light import Light

class Junction():

    id = 1
    entryJunctions = []

    def __init__(self, isEntryJunction: bool=False) -> None:
        self._id = Junction.id
        self._neighbouringJunctions = []
        self._trafficLightsInJunction = []
        self._isEntryJunction = isEntryJunction
        if (self._isEntryJunction):
            Junction.entryJunctions.append(self)
        Junction.id += 1


    def __repr__(self) -> str:
        return f"Junction id: {self._id}"

    
    #methods for creating, removing, and viewing junction neighbour pairs
    #possibly add limit to number of Junctions in NeighbouringJunctions (logically cannot be more than 4)
    def addJunctionNeighbourPair(self, neighbouringJunctionToAdd: "Junction"=None) -> None:
        if (neighbouringJunctionToAdd == None):
            neighbouringJunctionToAdd = Junction()

        try:
            if not isinstance(neighbouringJunctionToAdd, Junction):
                raise TypeError
               
            #calls the method again on the neighbouringJunctionToAdd object, using the current object as input
            #a loop is avoided as once the neighbouringJunctionToAdd object calls the method again, the Junctions are in the list and this block of code is skipped.
            if neighbouringJunctionToAdd not in self._neighbouringJunctions:
                self._neighbouringJunctions.append(neighbouringJunctionToAdd)
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


    def checkIfEntryJunction(self) -> bool:
        return self._isEntryJunction


    @staticmethod
    def getEntryJunctions() -> list:
        return Junction.entryJunctions

    #makes an entry junction a regular junction
    @staticmethod
    def removeEntryJunction(junctionToRemove: "Junction") -> None:
        try:
            if not isinstance(junctionToRemove, Junction):
                raise TypeError

            if (junctionToRemove.checkIfEntryJunction()):
                junctionToRemove._isEntryJunction = False
                Junction.entryJunctions.remove(junctionToRemove)

        except TypeError:
            print("TypeError: Input to removeEntryJunction method must be an instance of Junction class")
        return

    
    #methods for adding and removing traffic lights to junctions trafficLightsInJunction list
    def addTrafficLight(self, destinationJunction) -> None:
        try:
            if not isinstance(destinationJunction, Junction):
                raise TypeError

            trafficLight = Light(self, destinationJunction)
            if trafficLight in self._trafficLightsInJunction:
                del(trafficLight)
            else:
                self._trafficLightsInJunction.append(trafficLight)

        except TypeError:
            print("TypeError: Input to addTrafficLight method must be an instance of Junction class")
        return

    def removeTrafficLight(self, trafficLightToRemoveId: int) -> None:
        try:
            if not isinstance(trafficLightToRemoveId, int):
                raise TypeError
                
            for light in self._trafficLightsInJunction:
                if (light.getId() == trafficLightToRemoveId):
                    self._trafficLightsInJunction.remove(light)
                    print(f"{light} removed from {self}")
                else:
                    print(f"Light with id {trafficLightToRemoveId} not found in {self}")
        except TypeError:
            print("TypeError: input must be of type int")
        return

    #get list of traffic lights in junction
    def getTrafficLights(self) -> list:
        return self._trafficLightsInJunction

