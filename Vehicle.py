from junction import Junction
import random

class Vehicle():

    #fast and slow reaction times
    driverReactionTime = [(1, 2), (2, 3)]

    def __init__(self) -> None:
        self._route = Vehicle.setRoute()
        self._behaviour = random.choice(Vehicle.driverReactionTime)
        self._currentLight = None

    def __repr__(self) -> str:
        pass

    def getRoute(self) -> list:
        return self._route

    def getBehaviour(self) -> tuple:
        return self._behaviour

    
    def enterJunction(self) -> None:
        if (len(self._route) == 0):
            #exit the system
            pass
        junctionToEnter = self._route[0]
        for light in junctionToEnter.getTrafficLights():
            if (light.getDestination() == self._route[1]):
                light.addVehicle()
                self._currentLight = light
        return

    @staticmethod
    def setRoute() -> list:
        #chooses a hard coded route for D3, but will be updated to generate its own route based
        #on the junction layout for D4
        routes = [[1, 2, 3], [1, 4, 3], [3, 2, 1], [3, 4, 1]]
        return random.choice(routes)
    

if __name__ == "__main__":
    testVehicle = Vehicle()
    