class shape:
    def area(self):
        pass
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius  
class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
shapes = [circle(5), rectangle(4,7)]
for shape in shapes:
    print(f"The area is: {shape.area():.2f}")