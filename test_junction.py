import unittest
from junction import Junction

class TestJunction(unittest.TestCase):

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
        testJunction1 = Junction(isEntryJunction=True)
        badInput = "TestString"
        
        self.assertRaises(TypeError, Junction.removeEntryJunction(badInput))





if __name__ == "__main__":
    unittest.main()