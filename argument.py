def greet(name,age:int=25):
    return f"{name},{age}"
result1=greet("alice")
result2=greet("bob",30)
print(result1)
print(result2)