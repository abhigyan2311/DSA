'''
Singleton is a creational design pattern that lets you ensure 
that a class has only one instance, while providing a global 
access point to this instance.
'''

import threading

class MyClass:
    instance = None

    class _OnlyOne:
        def __init__(self) -> None:
            self._lock = threading.Lock()

    def __init__(self) -> None:
        # Singleton
        if not MyClass.instance:
            MyClass.instance = MyClass._OnlyOne()
        else:
            # Instance already instantiated
            pass