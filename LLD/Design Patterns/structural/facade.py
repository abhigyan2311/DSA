'''
Facade is a structural design pattern that provides a simplified interface
to a library, a framework, or any other complex set of classes.
'''

class Washing:
    '''Subsystem # 1'''
 
    def wash(self):
        print("Washing...")
 
 
class Rinsing:
    '''Subsystem # 2'''
 
    def rinse(self):
        print("Rinsing...")
 
 
class Spinning:
    '''Subsystem # 3'''
 
    def spin(self):
        print("Spinning...")
 
 
class WashingMachine:
    '''Facade'''
 
    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()
 
    def startWashing(self):
        self.washing.wash()
        self.rinsing.rinse()
        self.spinning.spin()
 
""" main method """
if __name__ == "__main__":
 
    washingMachine = WashingMachine()
    washingMachine.startWashing()