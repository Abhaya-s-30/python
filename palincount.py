def palindrome(input):
    string=input.replace(" ","").lower()
    return string==string[::-1]
def char_count(input):
    count={}
    for char in input:
        if char.isalnum():
            count[char]=count.get(char,0)+1
    return count
userinput=input("enter a string:")
if palindrome(userinput):
    print("palindrome")
else:
    print("not a palindrome")
character_count=char_count(userinput)
print(f"character counts: {character_count}")