from .vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, name, color="blue", wheel_size=30):
        super(Bike, self).__init__(name, color, wheel_size)

    def move(self):
        self._pedal()

    def _pedal(self):
        print("Pedalling " + self._name)