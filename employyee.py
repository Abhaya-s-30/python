class employee:
    def set_details(self,name,salary):
        self.name=name
        self.salary=salary
    def get_info(self):
        return f"name:{self.name},salart:{self.salary}"
class manager(employee):
    def set_department(self,department):
        self.department=department
    def get_info(self):
        return f"manager:{self.name}, salary:{self.salary}, department:{self.department}"
manager=manager()
manager.set_details("john",80000)
manager.set_department("sales")
print(manager.get_info())