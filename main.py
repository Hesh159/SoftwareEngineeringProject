from light import Light
from junction import Junction
from setup import mainSetup
from Vehicle import Vehicle
from TrafficLightController import TrafficLightController
import threading 
import time

class Main():

    def __init__(self) -> None:
        mainSetup()
        trafficLightController = TrafficLightController()
        print(Junction.junctions)
        for junction in Junction.junctions:
            thread = threading.Thread(target=trafficLightController.controller, args=(junction,))
            thread.daemon = True
            thread.start()

        while True:
            time.sleep(30)

        #create thread for generating vehicles


if __name__ == "__main__":
    main = Main()
        
