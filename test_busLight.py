from busLight import Light

def test_busLight_init():
    busLight = busLight()
    assert isinstance(busLight, Light)

def test_busLight_repr():
    busLight = busLight()
    assert isinstance(busLight.__repr__(), str)

def test_busLight_changeTrafficLightState():
    busLight = busLight()
    assert busLight.changeTrafficLightState(addAmount=2) == 2