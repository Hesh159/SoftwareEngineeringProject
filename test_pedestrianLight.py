from pedestrianLight import PedestrianLight

#test 1: check that the initial state of the light is 0 (red)
def test_initial_state():
    testTrafficLight = PedestrianLight()
    assert testTrafficLight.getState() == 0

#test 2: check that the buttonPress method changes the state of the light
def test_buttonPress():
    testTrafficLight = PedestrianLight()
    testTrafficLight.buttonPress()
    assert testTrafficLight.getState() == 1

#test 3: check that the checkLights method changes the state of the light
def test_checkLights():
    testTrafficLight = PedestrianLight()
    testTrafficLight._lightXRed = True
    testTrafficLight._lightYRed = True
    testTrafficLight.checkLights()
    assert testTrafficLight.getState() == 1

#test 4: check that the turnGreen method changes the state of the light
def test_turnGreen():
    testTrafficLight = PedestrianLight()
    testTrafficLight.turnGreen()
    assert testTrafficLight.getState() == 2

#test 5: check that the changeTrafficLightState method changes the state of the light
def test_changeTrafficLightState():
    testTrafficLight = PedestrianLight()
    testTrafficLight.changeTrafficLightState()
    assert testTrafficLight.getState() == 2