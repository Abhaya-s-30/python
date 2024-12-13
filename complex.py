class complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __add__(self,other):
        return complex(self.real+other.real, self.imag+other.imag)
    def __str__(self):
        return f"{self.real}+{self.imag}i"
c1=complex(3,4)
c2=complex(1,2)
result=c1+c2
print(result)