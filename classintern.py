class Employee:
    def work(self):
        print("Employee is working.")
class Manager(Employee):
    def work(self):
        print("Manager is managing the team.")
        super().work() 
class Intern(Employee):
    pass
def describe_work(employee):
    print(f"Description for {employee.__class__.__name__}:")
    employee.work()
employee = Employee()
manager = Manager()
intern = Intern()
describe_work(employee)
describe_work(manager)
describe_work(intern)
