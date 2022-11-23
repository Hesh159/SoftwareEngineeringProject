
class Light:
    
    id = 1
    trafficLightStates = ["Green", "Amber", "Red", "Idle"]

    #Light is initialized at Idle state
    def __init__(self, sourceJunction, destJunction) -> None:
        self._trafficLightStatePointer = 3
        self._currentTrafficLightState = Light.trafficLightStates[self._trafficLightStatePointer]
        self._currentCarsAtLight = 0
        self._maxCarsAtLight = 15
        self._sourceJunction = sourceJunction
        self._destinationJunction = destJunction
        self._id = Light.id
        Light.id += 1
        

    def __repr__(self) -> None:
        return f"Id {self._id}\nSource Junction: {self._sourceJunction} \nDestination Junction: {self._destinationJunction}"


    def __eq__(self, light) -> bool:
        if (self._sourceJunction == light._sourceJunction) and (self._destinationJunction == light._destinationJunction):
            return True
        return False


    def getId(self) -> int:
        return self._id

    def getLightDestination(self):
        return self._destinationJunction

    def addVehicle(self) -> None:
        self._currentCarsAtLight += 1

    #cycles through the light states by adding to trafficLightStatePointer and getting the modulas
    #as subclasses pedestrianLight and busLight do not have an amber state, the addAmount and modAmount
    #are changed slightly when called by these classes in order to skip amber.
    #for Light: addAmount = 1, modAmount = 3, for subclasses: addAmount = 2, modAmount = 4
    #honestly could be implemented better we may have to come back to this
    def changeTrafficLightState(self, addAmount=1) -> None:
        modAmount = addAmount + 2

        if self._trafficLightStatePointer == 3: #if light is currently in idle mode
            self._trafficLightStatePointer = 2
        else:
            self._trafficLightStatePointer += addAmount
            self._trafficLightStatePointer %= modAmount
        self._currentTrafficLightState = Light.trafficLightStates[self._trafficLightStatePointer]

    def getCurrentTrafficLightState(self) -> str:
        return self._currentTrafficLightState

    def enterIdleMode(self) -> None:
        self._trafficLightStatePointer = 3
        self._currentTrafficLightState = Light.trafficLightStates[self._trafficLightStatePointer]





def trafficLightStateChangeTests(numChanges, testTrafficLight):
    print("Testing traffic light state changes...")
    print("Printing current state...")
    print(testTrafficLight.getCurrentTrafficLightState())
    print("")

    for i in range(numChanges):
        print("Changing current state...")
        testTrafficLight.changeTrafficLightState()
        print("Printing current state...")
        print(testTrafficLight.getCurrentTrafficLightState())
        print("")

    #testing enterIdleMode method
    print("\nEntering idle mode...")
    testTrafficLight.enterIdleMode()
    print("Printing current state...")
    print(testTrafficLight.getCurrentTrafficLightState())
    print("")

    #leaving idle mode
    print("Changing current state...")
    testTrafficLight.changeTrafficLightState()
    print("Printing current state...")
    print(testTrafficLight.getCurrentTrafficLightState())
    print("\n")

    print("Completed testing traffic light state changes")




if __name__ == "__main__":
    testTrafficLight = Light()
    trafficLightStateChangeTests(5, testTrafficLight)
