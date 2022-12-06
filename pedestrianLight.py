from light import Light
import time

class PedestrianLight(Light):

    trafficLightStates = ["Green", "Red", "Idle"]

    def __init__(self, sourceJunction) -> None:
        super().__init__(sourceJunction=sourceJunction, prevJunction=None, destJunction=None) #Inherits
        self._buttonPressed = False
        self._blinkingLight = False
        self._lightXRed = False #check if left light is red
        self._lightYRed = False #check if right light is red
        self._junction = sourceJunction

    '''def __repr__(self) -> None:
        super().__repr__()'''           #I am unsure about the ID since it will be different to light.py, 
                                        #no junctions either since this light is not directional

    def button(self):
        if '''read input''':
            self._buttonPressed = True
        else:
            self._buttonPressed = False

    def buttonPress(self):
        if self._buttonPressed == True:
            pass
            #alert other lights that they should go red

    def checkLights(self):
        if (self._lightXRed == True) & (self._lightYRed == True):
            self._turnGreen()

    def turnGreen(self):
        time.sleep(5) #Wait 5 seconds before turning green
        #change light state to 1 green
        time.sleep(20)
        self._blinkingLight = True #This is for GUI class
        time.sleep(10) #10 seconds of blinking
        #change light state to 2 red
        self._blinkingLight = False
        self._buttonPressed = False #Reset variables

    def changeTrafficLightState(self) -> None:
        return super().changeTrafficLightState(addAmount=2)

    
    
# temp tests
if __name__ == "__main__":
    testTrafficLight = PedestrianLight()