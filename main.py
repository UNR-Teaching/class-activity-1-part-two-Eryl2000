from vehicles import Car, Bike

def main():
    car = Car("Ford Pinto")
    bike = Bike("BMX")

    vehicles = [car, bike]

    for vehicle in vehicles:
        vehicle.start()
        vehicle.move()
        vehicle.stop()


if __name__ == "__main__":
    main()