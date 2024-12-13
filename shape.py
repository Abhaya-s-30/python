class shape():
    def perimeter(self):
        raise NotImplementedError("subclass will override")
class triangle(shape):
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
    def perimeter(self):
        return self.side1+self.side2+self.side3
class square(shape):
    def __init__(self,side):
        self.side=side
    def perimeter(self):
        return 4*self.side
class rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def perimeter(self):
        return 2*(self.length+self.width)
shapes=[triangle(3,4,5),
        square(4),
        rectangle(5,3)]
for shape in shapes:
    print(f"{shape.__class__.__name__},perimeter:{shape.perimeter()}")