import abc

class Vehicle():
    def __init__(self, name, color, wheel_size):
        self._name = name
        self._color = color
        self.wheels = Wheels(wheel_size)

    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color

    @abc.abstractmethod
    def move(self):
        pass

    def start(self):
        print("Starting " + self._name)
    
    def stop(self):
        print("Stopping " + self._name)

class Wheels():
    def __init__(self, size):
        self.size = size

