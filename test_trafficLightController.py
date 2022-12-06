from TrafficLightController import TrafficLightController

#Test 1 - Check that the controller() function is looping
def test_controller_looping():
    tlc = TrafficLightController()
    junction = Junction()
    tlc.controller(junction)
    assert tlc.controller(junction) == True

#Test 2 - Check that the getCarsWaiting() function is returning the expected values
def test_getCarsWaiting():
    tlc = TrafficLightController()
    lightList = [Light(1, "red"), Light(2, "green")]
    assert tlc.getCarsWaiting(lightList) == 0
    lightList[1].setCarsAtLight(5)
    assert tlc.getCarsWaiting(lightList) == 5

#Test 3 - Check that the changeLightStates() function is changing states correctly
def test_changeLightStates():
    tlc = TrafficLightController()
    lightList = [Light(1, "red"), Light(2, "green")]
    tlc.changeLightStates(lightList)
    assert lightList[0].getCurrentState() == "amber"
    assert lightList[1].getCurrentState() == "red"

