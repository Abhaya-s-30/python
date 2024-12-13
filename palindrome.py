palindrome=lambda s:s==s[::-1]
word="malayalam"
result=palindrome(word)
print(f"is {word} a palindirme : {'yes' if result else 'no'}")