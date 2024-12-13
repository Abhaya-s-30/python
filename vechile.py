class Vehicle:
    def fuel_type(self):
        raise NotImplementedError("Subclass must implement fuel_type() method.")
class Car(Vehicle):
    def fuel_type(self):
        print("Car uses Petrol.")
class Bike(Vehicle):
    def fuel_type(self):
        print("Bike uses Electric.")
class Truck(Vehicle):
    def fuel_type(self):
        print("Truck uses Diesel.")
vehicles = [Car(), Bike(), Truck()]
for vehicle in vehicles:
    vehicle.fuel_type()
