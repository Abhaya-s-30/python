are_anagrams = lambda str1, str2: sorted(str1) == sorted(str2)
result = are_anagrams("listen", "silent")
print(result)