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
        




if __name__ == "__main__":
    unittest.main()