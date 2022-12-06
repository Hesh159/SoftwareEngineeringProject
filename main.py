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
        print(Junction.junctions)
        for junction in Junction.junctions:
            thread = threading.Thread(target=TrafficLightController.controller, args=(junction,))
            thread.start()
        #create thread for generating vehicles


if __name__ == "__main__":
    main = Main()
        
