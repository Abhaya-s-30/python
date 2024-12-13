class appliance:
    def __init__(self,brand):
        self.brand=brand
    def use(self):
        print("this is used for general purpose")
class washingmachine(appliance):
    def use(self):
        print(f"the {self.brand} washing machine is used for washing clothes")
class refrigerator(appliance):
    def use(self):
        print(f"the {self.brand} refrigerator is used for cooling foods")
washing_machine=washingmachine("samsung")
refrigerator=refrigerator("lg")
washing_machine.use()
refrigerator.use()