class A:
    def show(self):
        print("Class A")
class B(A):
    def display(self):
        print("Class B")
class C(B):
    def greet(self):
        print("Class C")
c_instance = C()
c_instance.greet()   
c_instance.display() 
c_instance.show()    
