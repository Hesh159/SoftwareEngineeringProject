
class Light:
    
    id = 1
    trafficLightStates = ["Green", "Amber", "Red", "Idle"]

    #Light is initialized at Idle state
    def __init__(self, sourceJunction, destJunction, prevJunction) -> None:
        self._trafficLightStatePointer = 3
        self._currentTrafficLightState = Light.trafficLightStates[self._trafficLightStatePointer]
        self._currentCarsAtLight = 0
        self._maxCarsAtLight = 15
        self._sourceJunction = sourceJunction
        self._destinationJunction = destJunction
        self._prevJunction = prevJunction
        self._cyclesWithoutCar = 0
        self._vehicleQueue = []
        self._id = Light.id
        Light.id += 1
        

    def __repr__(self) -> str:
        return f"Source: {self._sourceJunction} \tDest: {self._destinationJunction} \tPrev: {self._prevJunction}\n"

    def __str__(self) -> str:
        return f"Id: {self._id}\tState: {self._currentTrafficLightState}"

    def __eq__(self, light) -> bool:
        if (light == None):
            return False
        if (self._sourceJunction == light._sourceJunction) and (self._destinationJunction == light._destinationJunction) and (self._prevJunction == light._prevJunction):
            return True
        return False


    def getId(self) -> int:
        return self._id

    def getLightDestination(self):
        return self._destinationJunction

    def addVehicle(self, vehicle) -> None:
        self._currentCarsAtLight += 1
        self._vehicleQueue.append(vehicle)

    def removeVehicle(self) -> None:
        self._currentCarsAtLight -= 1
        self._vehicleQueue.pop(0)

    def getVehicleQueue(self) -> list:
        return self._vehicleQueue

    def getCarsAtLight(self) -> int:
        return self._currentCarsAtLight

    #for testing purposes only
    def setCarsAtLight(self, carsAtLight) -> None:
        self._currentCarsAtLight = carsAtLight

    def getMaxCarsAtLight(self) -> int:
        return self._maxCarsAtLight

    def setMaxCarsAtLight(self, newMaxCarsNum) -> None:
        self._maxCarsAtLight = newMaxCarsNum

    def increaseCyclesWithoutCar(self) -> None:
        self._cyclesWithoutCar += 1

    def resetCyclesWithoutCar(self) -> None:
        self._cyclesWithoutCar = 0

    def getCyclesWithoutCar(self) -> int:
        return self._cyclesWithoutCar

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

    def getCurrentState(self) -> str:
        return self._currentTrafficLightState

    def enterIdleMode(self) -> None:
        self._trafficLightStatePointer = 3
        self._currentTrafficLightState = Light.trafficLightStates[self._trafficLightStatePointer]
