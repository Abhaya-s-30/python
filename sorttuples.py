tuples = [(1, 2), (4, 5), (1, 1), (2, 3)]
sorted_tuples = sorted(tuples, key=lambda x: sum(x))
print(sorted_tuples)