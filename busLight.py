from light import Light

class busLight(Light):

    def __init__(self) -> None:
        super().__init__()

    def __repr__(self) -> str:
        return super().__repr__()

    
    def changeTrafficLightState(self, addAmount=1) -> None:
        return super().changeTrafficLightState(addAmount=2)