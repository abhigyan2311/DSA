class Player:
    def __init__(self, name: str) -> None:
        self._name = name
        self._pos = 0
    
    @property
    def position(self) -> int:
        return self._pos
    
    @position.setter
    def position(self, value: int):
        self._pos = value
