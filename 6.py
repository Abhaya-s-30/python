class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model   
    def display(self):
        print(f"Device: {self.brand} {self.model}")
class Mobile(Device):
    def __init__(self, brand, model, mobile_type):
        super().__init__(brand, model)  
        self.mobile_type = mobile_type  
    def display(self):
        super().display()  
        print(f"Mobile Type: {self.mobile_type}")
class Tablet(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)  
        self.screen_size = screen_size  
    def display(self):
        super().display()  
        print(f"Screen Size: {self.screen_size} inches")
class SmartDevice(Mobile, Tablet):
    def __init__(self, brand, model, mobile_type, screen_size):
        Mobile.__init__(self, brand, model, mobile_type)
        Tablet.__init__(self, brand, model, screen_size)    
    def display(self):
        super().display() 
smart_device = SmartDevice("BrandX", "ModelY", "Smartphone", 10)
smart_device.display()
print("\nMethod Resolution Order (MRO):", SmartDevice.__mro__)
