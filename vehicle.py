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

class Car(Vehicle):
    def __init__(self, name, color="red", wheel_size=80):
        super(Car, self).__init__(name, color, wheel_size)
        self.engine = Engine(200)

    def move(self):
        self._apply_gas()

    def _apply_gas(self):
        print("Applying gas to " + self._name)

class Bike(Vehicle):
    def __init__(self, name, color="blue", wheel_size=30):
        super(Bike, self).__init__(name, color, wheel_size)

    def move(self):
        self._pedal()

    def _pedal(self):
        print("Pedalling " + self._name)

class Wheels():
    def __init__(self, size):
        self.size = size

class Engine():
    def __init__(self, horsepower):
        self.horsepower = horsepower
        self.started = False

