'''
Prototype is a creational design pattern that lets you copy
existing objects without making your code dependent on their classes.
'''

from abc import ABC, abstractmethod
from copy import copy
 
 
# class - Courses at GeeksforGeeks
class Courses_At_GFG(ABC):
     
    # constructor
    def __init__(self):
        self.id = None
        self.type = None
 
    @abstractmethod
    def course(self):
        pass
 
    @property
    def type(self):
        return self.type
 
    @property
    def id(self):
        return self.id
    
    @id.setter
    def id(self, sid):
        self.id = sid
 
    def clone(self):
        return copy(self)
 
# class - DSA course
class DSA(Courses_At_GFG):
    def __init__(self):
        super().__init__()
        self.type = "Data Structures and Algorithms"
 
    def course(self):
        print("Inside DSA::course() method")
 
# class - SDE Course
class SDE(Courses_At_GFG):
    def __init__(self):
        super().__init__()
        self.type = "Software Development Engineer"
 
    def course(self):
        print("Inside SDE::course() method.")
 
# class - Courses At GeeksforGeeks Cache
class Courses_At_GFG_Cache:
     
    # cache to store useful information
    cache = {}
 
    @staticmethod
    def get_course(sid):
        COURSE = Courses_At_GFG_Cache.cache.get(sid, None)
        return COURSE.clone()
 
    @staticmethod
    def load():
        sde = SDE()
        sde.set_id("1")
        Courses_At_GFG_Cache.cache[sde.get_id()] = sde
 
        dsa = DSA()
        dsa.set_id("2")
        Courses_At_GFG_Cache.cache[dsa.get_id()] = dsa
 
# main function
if __name__ == '__main__':
    Courses_At_GFG_Cache.load()
 
    sde = Courses_At_GFG_Cache.get_course("1")
    print(sde.get_type())
 
    dsa = Courses_At_GFG_Cache.get_course("2")
    print(dsa.get_type())