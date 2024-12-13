class engine:
    def __init__(self,horsepower):
        self.horsepower=horsepower
class wheels:
    def __init__(self,count):
        self.count=count
class car(engine,wheels):
    def __init__(self,horsepower,count):
        engine.__init__(self,horsepower)
        wheels.__init__(self,count)
    def display(self):
        return f"car specification:\nhorsepower:{self.horsepower} hp \nno of wheels:{self.count}"
my_car=car(150,4)
print(my_car.display())