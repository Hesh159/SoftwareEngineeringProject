from light import Light
from light import trafficLightStateChangeTests

class PedestrianLight(Light):

    def __init__(self) -> None:
        super().__init__()

    def __repr__(self) -> None:
        super().__repr__()


    def changeTrafficLightState(self) -> None:
        return super().changeTrafficLightState()

    
    
# temp tests
if __name__ == "__main__":
    testTrafficLight = PedestrianLight()
    trafficLightStateChangeTests(5, testTrafficLight)