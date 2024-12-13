words = ["apple", "banana", "cherry", "date"]
group_by_length = lambda w: {length: [word for word in w if len(word) == length] for length in set(map(len, w))}
result = group_by_length(words)
print(result)
