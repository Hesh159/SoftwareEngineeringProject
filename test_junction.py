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
        




if __name__ == "__main__":
    unittest.main()