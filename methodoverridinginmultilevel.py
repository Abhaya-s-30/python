class shape:
    def area(self):
        print("area calculation not defined")
class quadrilateral(shape):
    def area(self):
        print("area calculation not implemrnted")
class rectangle(quadrilateral):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
length=float(input("enter length:"))
width=float(input("enter width"))
rectangle=rectangle(length,width)
print(f"area={rectangle.area()}")