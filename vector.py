class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y
vector1 = Vector(3, 4)
vector2 = Vector(1, 2)
dot_product = vector1 * vector2 
print(f"Dot Product: {dot_product}")
