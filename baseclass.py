class Base1:
    def calculate(self):
        print("Base1's calculate method")
class Base2(Base1):
    def calculate(self):
        print("Base2's calculate method")
        super().calculate()  
class Derived(Base2):
    def calculate(self):
        print("Derived's calculate method")
        super().calculate()  
derived_instance = Derived()
derived_instance.calculate()