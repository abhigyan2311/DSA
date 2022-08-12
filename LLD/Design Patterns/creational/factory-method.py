'''
Factory Method is a creational design pattern that provides an interface for 
creating objects in a superclass, but allows subclasses to alter the type of 
objects that will be created.
'''

from abc import ABC, abstractmethod

class IPerson(ABC):
    @abstractmethod
    def personType(self):
        pass

class Student(IPerson):
    def __init__(self, name) -> None:
        self._name = name
    
    def personType(self):
        return f"I am a student: {self._name}"

class Teacher(IPerson):
    def __init__(self, name) -> None:
        self._name = name
    
    def personType(self):
        return f"I am a teacher: {self._name}"

class PersonFactory:
    @staticmethod
    def buildPerson(name, personType):
        if personType=="Student": return Student(name)
        elif personType=="Teacher": return Teacher(name)
        return -1