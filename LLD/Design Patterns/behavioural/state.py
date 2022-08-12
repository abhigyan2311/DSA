'''
State is a behavioral design pattern that lets an object alter its behavior 
when its internal state changes. It appears as if the object changed its class.
'''

from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def think(self):
        pass

class HappyState(State):
    def think(self):
        return "I am happy"

class SadState(State):
    def think(self):
        return "I am sad"

class Human():
    def __init__(self) -> None:
        self.state = SadState()
    
    def think(self):
        return self.state.think()

human = Human()
print(human.think())