from junction import Junction
from setup import mainSetup
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

    def enterNextJunction(self) -> None:
        if len(self._route) <= 3:
            print("Vehicle Leaving System")
            del(self)
        else:
            nextJunction = self._route[1]
            for light in nextJunction.getTrafficLights():
                if light.getLightDestination() == self._route[2]:
                    if self._currentLight != None:
                        self._currentLight.removeVehicle()
                    light.addVehicle(self)
                    self._currentLight = light
                    self._route = self._route[1:]
        return

    @staticmethod
    def setRoute() -> list:
        route = []
        entryJunctions = Junction.getEntryJunctions().copy()
        random.shuffle(entryJunctions)
        entryJunction = entryJunctions[0]
        junction = entryJunction
        exitJunction = entryJunctions[1]
        route.append(entryJunction)
        while exitJunction not in junction.getNeighbouringJunctions():
            newJunction = random.choice(junction.getNeighbouringJunctions())
            if newJunction not in route:
                route.append(newJunction)
                junction = newJunction
        route.append(exitJunction)
        return route

if __name__ == "__main__":
    mainSetup()
    testVehicle = Vehicle()
    