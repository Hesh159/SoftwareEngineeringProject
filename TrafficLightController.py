from junction import Junction
from light import Light
from time import sleep
import threading
class TrafficLightController():

    def __init__(self) -> None:          
        self._baseTimePerCar = 2


    def controller(self, junctionToControl):
        connectedLights = junctionToControl.getConnectedLightLists()
        numberOfChangesPerCycle = len(connectedLights)   #change this to only change when pedestrian light
                                                                                    #is pressed for junctions with only 2 neighbours
        baseTimePerCar = 2

        while True:
            for connectedLightSet in connectedLights: #connectedLights is a dict and connectedLightSet is a key for the dict
                                                        #the list of lights can be found in connectedLights[connectedLightSet]
                lightList = connectedLights[connectedLightSet]

                carsWaiting = self.getCarsWaiting(lightList)
                timeElapsed = 0

                self.changeLightStates(lightList)   #change to green
                while timeElapsed < baseTimePerCar * carsWaiting:
                    for light in lightList:
                        vehicleQueue = light.getVehicleQueue()
                        if len(vehicleQueue) != 0:
                            vehicleToMove = light.getVehicleQueue()[0]
                            vehicleToMove.enterNextJunction()
                    sleep(2)
                    timeElapsed += 2
                self.changeLightStates(lightList)   #change to amber
                for light in lightList:
                    vehicleQueue = light.getVehicleQueue()
                    if len(vehicleQueue) != 0:
                        vehicleToMove = light.getVehicleQueue()[0]
                        vehicleToMove.enterNextJunction()
                self.changeLightStates(lightList)            #change to red
                
                
                #checkPedestrianLight
                #if checked start pedestrian light
                if len(junctionToControl.pedLight) != 0:
                    pedestrianLight = junctionToControl.pedLight[0]
                    if pedestrianLight._buttonPressed == True:
                        pedestrianLight.changeTrafficLightState()
                        sleep(10)
                        pedestrianLight.changeTrafficLightState()

    def getCarsWaiting(self, lightList):
        carsWaiting = 0
        for light in lightList:
            carsAtLight = light.getCarsAtLight()
            if carsAtLight == 0:
                light.increaseCyclesWithoutCar()
            else:
                light.resetCyclesWithoutCar()
            if carsAtLight > carsWaiting:
                carsWaiting = carsAtLight
        return carsWaiting

    def changeLightStates(self, lightList):
        for light in lightList:
            if light.getCurrentState() == "Idle":
                light.changeTrafficLightState()
                light.changeTrafficLightState()
            else:
                light.changeTrafficLightState()

    def controllerTest(self, lights):
        baseTimePerCar = 0.1
        lightList = lights
        carsWaiting = self.getCarsWaiting(lightList)
        self.changeLightStates(lightList)  
        sleep(baseTimePerCar * carsWaiting)
        self.changeLightStates(lightList)   
        sleep(baseTimePerCar)
        self.changeLightStates(lightList)           







