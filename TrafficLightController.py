from junction import Junction
from light import Light

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
        return carsWaiting + 1    

    def changeLightStates(self, lightList):
        for light in lightList:
            if light.getCurrentState() == "idle":







