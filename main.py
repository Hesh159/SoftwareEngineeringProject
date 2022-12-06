from light import Light
from junction import Junction
from setup import mainSetup
from Vehicle import Vehicle
from TrafficLightController import TrafficLightController
import threading 
import time
import random
import multiprocessing

class Main():

    def __init__(self) -> None:
        mainSetup()
        trafficLightController = TrafficLightController()
        for junction in Junction.junctions:
            thread = threading.Thread(target=trafficLightController.controller, args=(junction,))
            thread.daemon = True
            thread.start()
        vehicleGeneration = multiprocessing.Process(target=self.generateVehicles())
        vehicleGeneration.start()

        while True:
            time.sleep(30)

        #create thread for generating vehicles

    def generateVehicles(self) -> None:
        while True:
            randint = random.randint(0, 3)
            for i in range(randint):
                vehicle = Vehicle()
                vehicle.enterNextJunction()
            randSleep = random.randint(2, 4)
            time.sleep(randSleep)


if __name__ == "__main__":
    main = Main()
        
