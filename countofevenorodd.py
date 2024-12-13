def count_even_odd(numbers):
    even_count=0
    odd_count=0
    for number in numbers:
        if number%2==0:
            even_count+=1
        else:
            odd_count+=1
    return even_count,odd_count
user_input=input("enter a list of numbers ")
numbers=[int(num) for num in user_input.split()]
even_count,odd_count=count_even_odd(numbers)
print(f"even count:{even_count},odd count:{odd_count}")