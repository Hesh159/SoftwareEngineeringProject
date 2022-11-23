import unittest
from light import Light
from junction import Junction

class TestLight(unittest.TestCase):

    sourceJunction = Junction()
    destJunction = Junction()

    def test_eqMethod(self):
        testLight1 = Light(TestLight.sourceJunction, TestLight.destJunction)
        testLight2 = Light(TestLight.sourceJunction, TestLight.destJunction)

        self.assertTrue(testLight1 == testLight2)


    #test trafficLightStateChanges
    def test_TrafficLightLeavingIdleMode(self):
        testLight = Light(TestLight.sourceJunction, TestLight.destJunction)
        testLight.changeTrafficLightState()
        expectedResult = "Red"
        actualResult = testLight.getCurrentState()

        self.assertEqual(actualResult, expectedResult)

    def test_changeToGreen(self):
        testLight = Light(TestLight.sourceJunction, TestLight.destJunction)
        for i in range(2):
            testLight.changeTrafficLightState()
        expectedResult = "Green"
        actualResult = testLight.getCurrentState()

        self.assertEqual(actualResult, expectedResult)

    def test_changeToAmber(self):
        testLight = Light(TestLight.sourceJunction, TestLight.destJunction)
        for i in range(3):
            testLight.changeTrafficLightState()
        expectedResult = "Amber"
        actualResult = testLight.getCurrentState()

        self.assertEqual(actualResult, expectedResult)

    def test_changeToRed(self):
        testLight = Light(TestLight.sourceJunction, TestLight.destJunction)
        for i in range(4):
            testLight.changeTrafficLightState()
        expectedResult = "Red"
        actualResult = testLight.getCurrentState()

        self.assertEqual(actualResult, expectedResult)

    def test_enterIdleMode(self):
        testLight = Light(TestLight.sourceJunction, TestLight.destJunction)
        for i in range(2):
            testLight.changeTrafficLightState()
        testLight.enterIdleMode()
        expectedResult = "Idle"
        actualResult = testLight.getCurrentState()

        self.assertEqual(actualResult, expectedResult)
    


if __name__ == "__main__":
    unittest.main()