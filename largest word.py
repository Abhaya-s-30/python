sentence = "The quick brown fox jumps over the lazy dog"
longest_word = lambda s: max(s.split(), key=lambda x: len(x))
result = longest_word(sentence)
print(result)