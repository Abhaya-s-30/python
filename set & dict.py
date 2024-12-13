def frequency_dict(numbers):
    return {num: numbers.count(num) for num in set(numbers)}
numbers = [1, 2, 2, 3, 4, 4, 4]
print(frequency_dict(numbers))

my_dict = {'a': 10, 'b': 20, 'c': 30}
keys_set = set(my_dict.keys())
print(keys_set)

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 25, 'c': 35, 'd': 40}
common_keys = set(dict1.keys()) & set(dict2.keys())
print(common_keys)

my_dict = {'a': 10, 'b': 20, 'c': 30}
my_set = {10, 30, 40}
common_values = set(my_dict.values()) & my_set
print(common_values)

tuples_list = [('a', 1), ('b', 2), ('c', 3)]
my_dict = dict(tuples_list)
print(my_dict)

my_set = {'apple', 'banana', 'cherry'}
length_dict = {item: len(item) for item in my_set}
print(length_dict)

dict_list = [{'a': 1, 'b': 2}, {'a': 2, 'c': 3}, {'d': 4, 'b': 5}]
unique_values = set(value for d in dict_list for value in d.values())
print(unique_values)

my_dict = {'a': 1, 'b': 2, 'c': 3}
dict_tuples = set(my_dict.items())
print(dict_tuples)

my_string = "banana"
char_positions = {}
for index, char in enumerate(my_string):
    if char not in char_positions:
        char_positions[char] = set()
    char_positions[char].add(index)
print(char_positions)

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_set = set(my_dict.keys())
for key in keys_set:
    del my_dict[key]
print(my_dict)




