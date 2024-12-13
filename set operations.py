set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print("Union of the sets:", union_set)
intersection_set = set1 & set2
print("Intersection of the sets:", intersection_set)
difference_set = set1 - set2
print("Difference of the sets:", difference_set)
symmetric_difference_set = set1 ^ set2
print("Symmetric difference of the sets:", symmetric_difference_set)
is_subset = set1 <= set2
print("Is set1 a subset of set2?", is_subset)
is_superset = set1 >= set2
print("Is set1 a superset of set2?", is_superset)
are_disjoint = set1.isdisjoint(set2)
print("Are the sets disjoint?", are_disjoint)

numbers = [1, 2, 3, 4, 5, 6,6,7 ,7, 8]
even_squares = {num ** 2 for num in numbers if num % 2 == 0}
print("Squares of even numbers:", even_squares)

unique_count = len(set(numbers))
print("Number of unique elements:", unique_count)

unique_numbers = set(numbers)
print("Unique elements:", unique_numbers)

words = ['apple', 'banana', 'apple', 'cherry']
unique_words = set(words)
print("Unique words:", unique_words)

sets_list = [{1, 2}, {2, 3}, {3, 4}]
union_result = set()
for s in sets_list:
    union_result |= s
print("Union of sets:", union_result)

intersection_result = sets_list[0]
for s in sets_list[1:]:
    intersection_result &= s
print("Intersection of sets:", intersection_result)

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = set(list1) & set(list2)
print("Common elements:", common_elements)

my_string = "banana"
unique_chars = set(my_string)
print("Unique characters:", unique_chars)

def set_operations(set1, set2):
    union = set1 | set2
    intersection = set1 & set2
    difference = set1 - set2
    symmetric_difference = set1 ^ set2
    return union, intersection, difference, symmetric_difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union, intersection, difference, symmetric_difference = set_operations(set1, set2)
print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)
print("Symmetric Difference:", symmetric_difference)

my_set = {1, 2, 3, 4, 5}
element = 3
if element in my_set:
    print(f"{element} is present in the set.")
else:
    print(f"{element} is not present in the set.")

my_set = {1, 2, 3}
my_list = [4, 5, 6]
my_set.update(my_list)
print("Updated set:", my_set)

frozenset1 = frozenset([1, 2, 3, 4, 5])
frozenset2 = frozenset([4, 5, 6, 7, 8])
union_result = frozenset1 | frozenset2
print("Union of frozensets:", union_result)
intersection_result = frozenset1 & frozenset2
print("Intersection of frozensets:", intersection_result)

def generate_primes(n):
    primes = set()
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.add(num)
    return primes
n = 50
prime_numbers = generate_primes(n)
print(f"Prime numbers up to {n}:", prime_numbers)








