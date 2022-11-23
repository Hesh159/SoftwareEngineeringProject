import time
from Vehicle import Vehicle

class bus(Vehicle):

    def __init__(self) -> None:
        super().__init__()
    
    def getBehaviour(self) -> tuple:
        return (3,4)

if __name__ == "__name__":
    testbus = bus(Vehicle)
        