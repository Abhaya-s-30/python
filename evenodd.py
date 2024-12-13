def even_odd(number):
    if number%2==0:
        return "even"
    else:
        return"odd"
num=int(input("enter a number:"))
result=even_odd(num)
print(f"the number {num} is:{result}")