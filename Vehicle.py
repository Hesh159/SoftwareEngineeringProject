from random import randint
import random
import time

class Vehicle():

    #fast and slow reaction times
    driverReactionTime = [(1, 2), (2, 3)]

    def __init__(self) -> None:
        self._route = Vehicle.getRoute()
        self._behaviour = random.choose(Vehicle.driverReactionTime)

    def __repr__(self) -> str:
        pass

    def getRoute(self) -> list:
        return self._route

    def getBehaviour(self) -> tuple:
        return self._behaviour

    @staticmethod
    def setRoute() -> list:
        #chooses a hard coded route for D3, but will be updated to generate its own route based
        #on the junction layout for D4
        routes = [[1, 2, 3], [1, 4, 3], [3, 2, 1], [3, 4, 1]]
        return random.choose(routes)
    

if __name__ == "__main__":
    testVehicle = Vehicle()
    