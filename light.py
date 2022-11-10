
class Light:
    
    def __init__(self) -> None:
        self._trafficLightStates = ["Green", "Amber", "Red", "Idle"]
        self._trafficLightStatePointer = 3
        self._currentTrafficLightState = self._trafficLightStates[self._trafficLightStatePointer]

    def __repr__() -> None:
        pass

    
    def changeTrafficLightState(self, ) -> None:
        if self._trafficLightStatePointer == 3: #if light is currently in idle mode
            self._trafficLightStatePointer = 2
        else:
            self._trafficLightStatePointer += 1
            self._trafficLightStatePointer %= 3
        self._currentTrafficLightState = self._trafficLightStates[self._trafficLightStatePointer]

    def getCurrentTrafficLightState(self) -> str:
        return self._currentTrafficLightState

    def enterIdleMode(self) -> None:
        self._trafficLightStatePointer = 3
        self._currentTrafficLightState = self._trafficLightStates[self._trafficLightStatePointer]





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
