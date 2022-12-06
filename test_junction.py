import unittest
from junction import Junction
from light import Light

class TestJunction(unittest.TestCase):

    #addNeighbourPair tests
    def test_addJunctionNeighbourPairSuccessfully(self):
        testJunction1 = Junction()
        testJunction2 = Junction()
        testJunction1.addJunctionNeighbourPair(testJunction2)
        expectedResultList = [testJunction2]
        actualResultList = testJunction1.getNeighbouringJunctions()

        self.assertEqual(actualResultList, expectedResultList)

    def test_addJunctionNeighbourPairNoInput(self):
        testJunction1 = Junction()
        testJunction1.addJunctionNeighbourPair()
        expectedResultListSize = 1
        actualResultListSize = len(testJunction1.getNeighbouringJunctions())

        self.assertEqual(actualResultListSize, expectedResultListSize)

    def test_addJunctionNeighbourPairWrongInput(self):
        testjunction1 = Junction()
        WrongInput = 17

        self.assertRaises(TypeError, testjunction1.addJunctionNeighbourPair(WrongInput))
        
    #removeNeighbourPair tests
    def test_removeJunctionNeighbourPair(self):
        testjunction1 = Junction()
        testjunction2 = Junction()
        testjunction1.addJunctionNeighbourPair(testjunction2)
        testjunction1.removeJunctionNeighbourPair(testjunction2)
        expectedResultList = []
        actualResultList = testjunction2.getNeighbouringJunctions()

        self.assertEqual(actualResultList, expectedResultList)

    def test_removeJunctionNeighbourPairBadInput(self):
        testjunction1 = Junction()
        testjunction1.addJunctionNeighbourPair()
        badInput = "String"

        self.assertRaises(TypeError, testjunction1.removeJunctionNeighbourPair(badInput))

    #entry junction tests
    def test_checkIfEntryJunction(self):
        testjunction1 = Junction(isEntryJunction=True)
        actualResult = testjunction1.checkIfEntryJunction()

        self.assertEqual(actualResult, True)
    
    def test_getEntryJunctionStaticMethod(self):
        Junction.entryJunctions.clear()
        testjunction1 = Junction(isEntryJunction=True)
        testjunction2 = Junction(isEntryJunction=True)
        expectedResult = [testjunction1, testjunction2]
        actualResult = Junction.getEntryJunctions()

        self.assertEqual(actualResult, expectedResult)

    def test_removeEntryJunctionStaticMethod(self):
        Junction.entryJunctions.clear()
        testJunction1 = Junction(isEntryJunction=True)
        Junction.removeEntryJunction(testJunction1)
        expectedResult = []

        self.assertEqual(Junction.getEntryJunctions(), expectedResult)

    def test_removeEntryJunctionBadInput(self):
        Junction.entryJunctions.clear()
        badInput = "TestString"
        
        self.assertRaises(TypeError, Junction.removeEntryJunction(badInput))


    #add lights tests
    def test_addTrafficLightTest(self):
        testJunction1 = Junction()
        destinationJunction = Junction()
        prevJunction = Junction()
        testJunction1.addTrafficLight(destinationJunction=destinationJunction, prevJunction=prevJunction)
        expectedResultListSize = 1
        actualResultListSize = len(testJunction1.getTrafficLights())

        self.assertEqual(actualResultListSize, expectedResultListSize)

    def test_addTrafficLightCreatesLightObject(self):
        testJunction1 = Junction()
        destinationJunction = Junction()
        prevJunciton = Junction()
        testJunction1.addTrafficLight(destinationJunction=destinationJunction, prevJunction=prevJunciton)
        createdObject = testJunction1.getTrafficLights()[0]

        self.assertTrue(isinstance(createdObject, Light))

    def test_addTrafficLightWithDestJunctionBadInput(self):
        testJunction1 = Junction()
        badInput = "Shit input"
        prevJunction = Junction()
        
        self.assertRaises(TypeError, testJunction1.addTrafficLight(destinationJunction=badInput, prevJunction=prevJunction))

    def test_addTrafficLightWithPrevJunctionBadInput(self):
        testJunction = Junction()
        destJunction = Junction()
        badInput = "ghdh2"

        self.assertRaises(TypeError, testJunction.addTrafficLight(destinationJunction=destJunction, prevJunction=badInput))

    def test_addTrafficLightDuplicate(self):
        testJunction1 = Junction()
        destinationJunction = Junction()
        prevJunction = Junction()
        testJunction1.addTrafficLight(destinationJunction=destinationJunction, prevJunction=prevJunction)
        testJunction1.addTrafficLight(destinationJunction=destinationJunction, prevJunction=prevJunction)
        expectedResultListSize = 1
        actualResultListSize = len(testJunction1.getTrafficLights())

        self.assertEqual(actualResultListSize, expectedResultListSize)

    #removeTrafficLight test methods
    def test_removeTrafficLightTest(self):
        testJunction = Junction()
        destinationJunction = Junction()
        prevJunction = Junction()
        testJunction.addTrafficLight(destinationJunction=destinationJunction, prevJunction=prevJunction)
        lightToRemove = testJunction.getTrafficLights()[0]
        lightToRemoveId = lightToRemove.getId()
        testJunction.removeTrafficLight(lightToRemoveId)

        expectedResultListSize = 0
        actualResultListSize = len(testJunction.getTrafficLights())

        self.assertEqual(actualResultListSize, expectedResultListSize)

    def test_removeTrafficLightBadInput(self):
        testJunction = Junction()
        destJunction = Junction()
        prevJunction = Junction()
        testJunction.addTrafficLight(destinationJunction=destJunction, prevJunction=prevJunction)
        badInput = "This is bad input"

        self.assertRaises(TypeError, testJunction.removeTrafficLight(badInput))

    def test_addToConnectedLights(self):
        testJunction = Junction()
        destJunction = Junction()
        prevJunction = Junction()
        testJunction.addTrafficLight(destinationJunction=destJunction, prevJunction=prevJunction)
        expectedValuesInConnectedLights = 1
        actualValuesInConnectedLights = len(testJunction.getLightsFromJunction(prevJunction))

        self.assertEqual(expectedValuesInConnectedLights, actualValuesInConnectedLights)

    def test_removeFromConnectedLights(self):
        testJunction = Junction()
        destJunction = Junction()
        prevJunction  = Junction()
        testJunction.addTrafficLight(destinationJunction=destJunction, prevJunction=prevJunction)
        lightToRemove = testJunction._trafficLightsInJunction[0].getId()
        testJunction.removeTrafficLight(lightToRemove)

        expectedConnectedLightsSize = 0
        actualConnectedLightsSize = len(testJunction.getLightsFromJunction(prevJunction))

        self.assertEqual(expectedConnectedLightsSize, actualConnectedLightsSize)


if __name__ == "__main__":
    unittest.main()