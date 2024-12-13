class vehicle:
    def fuel_efficiency(self):
        pass
    def __str__(self):
        pass
class car(vehicle):
    def fuel_efficiency(self):
        return "car:15km/l"
    def __str__(self):
        pass
class bike(vehicle):
    def fuel_efficiency(self):
        return "bike:40km/l"
    def __str__(self):
        pass
vehicles=[car(),bike()]
for vehicle in vehicles:
    print(vehicle.fuel_efficiency())