class Vehicle:
    _wheels = 0
    _doors = 0

    def __init__(self) -> None:
        super(Vehicle, self).__init__()

    @property
    def wheelsOnThe(self):
        return self._wheels

    @property
    def doorsOnThe(self):
        return self._doors

    def moreWheels(self):
        self._wheels += 1

    def moreDoors(self):
        self._doors += 1


class Bike(Vehicle):
    def __init__(self) -> None:
        super(Bike, self).__init__()
        pass


class Car(Vehicle):
    def __init__(self) -> None:
        super(Car, self).__init__()
        pass


vehicleList = [
    Bike(),
    Car(),
    Vehicle(),
]


for _ in range(4):
    vehicleList[1].moreWheels()

for _ in range(2):
    vehicleList[0].moreWheels()
    vehicleList[1].moreDoors()

for v in vehicleList:
    print(f"There are {v.wheelsOnThe} wheels on the {type(v).__name__}")
    print(f"        & {v.doorsOnThe} doors on the {type(v).__name__}")


print(Vehicle._wheels)
print(Car._wheels)
print(Bike._wheels)
