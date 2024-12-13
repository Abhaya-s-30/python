class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class addition(calculator):
    def calculate(self):
        return self.a+self.b
class subtraction(calculator):
    def calculate(self):
        return self.a-self.b
class multiplication(calculator):
    def calculate(self):
        return self.a*self.b
class division(calculator):
    def calculate(self):
        if self.b==0:
            return "error"
        return self.a/self.b
add=addition(10,5)
sub=subtraction(10,5)
mul=multiplication(10,5)
div=division(10,5)
print("addition:",add.calculate())
print("subtraction:",sub.calculate())
print("multiplication:",mul.calculate())
print("division:",div.calculate())

