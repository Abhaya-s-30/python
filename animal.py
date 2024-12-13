class animal:
    def sound(self):
        return "animals make sound"
class dog(animal):
    def sound(self):
        return "dog barks"
class cat(animal):
    def sound(self):
        return "cat meows"
dog=dog()
cat=cat()
print(dog.sound())
print(cat.sound())