class a:
    def show(self):
        print("this show method from class a")
class b(a):
    def show(self):
        print("this show method class from b")
class c(a):
    def show(self):
        print("this show method from c")
class d(c,b):
    pass
obj=d()
obj.show()
print("\nmro")
print(d.mro())
