string=input("enter a string:-")
n=int(input("enter the index of the character:-"))
if 0<=n<len(string):
    nth_char=string[n]
    print(f"char at index {n} is:'{nth_char}'")
else:
    print("index out of range")