class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
class ColoredVector(Vector):
    def __init__(self, x, y, color):
        super().__init__(x, y)  
        self.color = color    
    def __str__(self):
        return f"ColoredVector({self.x}, {self.y}, {self.color})"
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
cv1 = ColoredVector(1, 1, "Red")
print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")
print(f"Added Vector: {v3}")
print(f"Colored Vector: {cv1}")
