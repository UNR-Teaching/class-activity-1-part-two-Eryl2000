from .vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, name, color="red", wheel_size=80):
        super(Car, self).__init__(name, color, wheel_size)
        self.engine = Engine(200)

    def move(self):
        self._apply_gas()

    def _apply_gas(self):
        print("Applying gas to " + self._name)

class Engine():
    def __init__(self, horsepower):
        self.horsepower = horsepower
        self.started = False