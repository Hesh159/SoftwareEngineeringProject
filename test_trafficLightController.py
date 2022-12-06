import unittest
from TrafficLightController import TrafficLightController
from junction import Junction
from light import Light
from setup import mainSetup

class TestTrafficLightController(unittest.TestCase):

    def test_getCarsWaiting(self):
        lights = testJunction.getTrafficLights()
        lights[0].setCarsAtLight(8)
        lights[1].setCarsAtLight(10)
        expectedResult = 10
        actualResult = TrafficLightController.getCarsWaiting(self, lights)

        self.assertEqual(expectedResult, actualResult)

    def test_getCarsWaitingIncreaseCycles(self):
        lights = testJunction.getTrafficLights()
        lights[0].setCarsAtLight(0)
        TrafficLightController.getCarsWaiting(self, lights)
        expectedResult = 1
        actualResult = lights[0].getCyclesWithoutCar()

        self.assertEqual(expectedResult, actualResult)

    def test_getCarsWaitingResetCycles(self):
        lights = testJunction.getTrafficLights()
        lights[0].setCarsAtLight(0)
        TrafficLightController.getCarsWaiting(self, lights)
        lights[0].setCarsAtLight(5)
        TrafficLightController.getCarsWaiting(self, lights)
        expectedResult = 0
        actualResult = lights[0].getCyclesWithoutCar()

        self.assertEqual(expectedResult, actualResult)

    def test_controller(self):
        controller = TrafficLightController()
        lights = testJunction.getTrafficLights()
        lights[0].setCarsAtLight(0)
        lights[1].setCarsAtLight(1)
        TrafficLightController.controllerTest(controller, lights)
        expectedResult = "Red"
        actualResult = lights[0].getCurrentState()

        self.assertEqual(expectedResult, actualResult)



if __name__ == "__main__":
    mainSetup()
    testJunction = Junction.junctions[0]
    unittest.main()