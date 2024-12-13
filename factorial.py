fact=lambda n:1 if n==0 else n*fact(n-1)
result=fact(5)
print(result)