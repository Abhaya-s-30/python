class animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        return"some sound"
class dog(animal):
    def __init__(self,name):
        super().__init__(name)
    def sound(self):
        return f"{self.name} barks"
dogs=dog("tommy")
print (dogs.sound())