class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def calculate_final_price(self):
        return self.price
class DigitalProduct(Product):
    def __init__(self, name, price, file_size):
        super().__init__(name, price)
        self.file_size = file_size
    def calculate_final_price(self):
        print(f"Calculating final price for Digital Product: {self.name}")
        return self.price  
class PhysicalProduct(Product):
    def __init__(self, name, price, weight, shipping_cost):
        super().__init__(name, price)
        self.weight = weight
        self.shipping_cost = shipping_cost
    def calculate_final_price(self):
        print(f"Calculating final price for Physical Product: {self.name}")
        return self.price + self.shipping_cost  
digital_product = DigitalProduct("E-Book", 10, "5MB")
physical_product = PhysicalProduct("Laptop", 1000, 2.5, 50)
final_price_digital = digital_product.calculate_final_price()
print(f"Final price of {digital_product.name}: ${final_price_digital}\n")
final_price_physical = physical_product.calculate_final_price()
print(f"Final price of {physical_product.name}: ${final_price_physical}")
