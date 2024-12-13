class bird:
    def fly(self):
        pass
    def __str__(self):
        return "this is a bird"
class sparrow(bird):
    def fly(self):
        return f"sparrow can fly fast"
    def __str__(self):
        return "this is a sparrow"
class ostrich(bird):
    def fly(self):
        return f" ostrich cannot fly"
    def __str__(self):
        return "this is a ostrich"
birds=[sparrow(),ostrich()]
for bird in birds:
    print(bird.fly())