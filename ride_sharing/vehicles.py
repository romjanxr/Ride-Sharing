from abc import ABC, abstractmethod


class Vehicle(ABC):
    speeds = {
        "car": 30,
        "bike": 50,
        "cng": 15
    }

    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.status = 'available'
        self.rate = rate
        self.driver = driver
        self.speed = self.speeds[vehicle_type]

    @abstractmethod
    def start_driving(self):
        pass

    @abstractmethod
    def trip_finish(self):
        pass


class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self):
        self.status = 'unavailable'
        print(self.vehicle_type, self.license_plate, "started")
        return super().start_driving()

    def trip_finish(self):
        self.status = 'available'
        print(self.vehicle_type, self.license_plate, "trip finished")


class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self):
        self.status = 'unavailable'
        print(self.vehicle_type, self.license_plate, "started")
        return super().start_driving()

    def trip_finish(self):
        self.status = 'available'
        print(self.vehicle_type, self.license_plate, "trip finished")


class Cng(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self):
        self.status = 'unavailable'
        print(self.vehicle_type, self.license_plate, "started")
        return super().start_driving()

    def trip_finish(self):
        self.status = 'available'
        print(self.vehicle_type, self.license_plate, "trip finished")
