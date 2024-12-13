class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self,other):
        return self.marks>other.marks
    def __str__(self):
        return f"student:{self.name},marks:{self.marks}"
s1=student("alice",85)
s2=student("bob",90)
print(s1>s2)