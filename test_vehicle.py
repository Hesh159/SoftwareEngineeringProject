import unittest
from Vehicle import Vehicle

class TestVehicle(unittest.TestCase):
    pass

#test that the route is set correctly
def test_route():
    assert TestVehicle.getRoute() == [1, 2, 3] or [1, 4, 3] or [3, 2, 1] or [3, 4, 1]


#test that the behaviour is set correctly
def test_behaviour():
    assert TestVehicle.getBehaviour() == (1, 2) or (2, 3)

if __name__ == "__main__":
    unittest.main()