string="hello world"
vowels={'a','e','i','o','u'}
vowels_in_string={char for char in string.lower() if char in vowels}
print("vowels:",vowels_in_string)
