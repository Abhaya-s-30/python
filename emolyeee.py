class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_info(self):
        print(f"name:{self.name}, age:{self.age}")
class manager(employee):
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.department=department
    def display_info(self):
        super().display_info()
        print(f"department: {self.department}")
class intern(employee):
    def __init__(self, name, age,university):
        super().__init__(name, age)
        self.university=university
    def display_info(self):
        super().display_info()
        print(f"university:{self.university}")
manager=manager("alice",35,"it")
intern=intern("cris",25,"harvard university")
print("manager details:")
manager.display_info()
print("\nintern details")
intern.display_info()