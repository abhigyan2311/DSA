import random

class Dice:
    def __init__(self, maxVal: int) -> None:
        self._maxVal = maxVal
    
    def roll(self) -> int:
        return random.randint(1, self._maxVal)