vowels=lambda s:len(list(filter(lambda x:x in 'aeiouAEIOU',s)))
text="hello world"
result=vowels(text)
print(f"num of vowels in {text}:{result}")