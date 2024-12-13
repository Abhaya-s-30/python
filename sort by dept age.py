employees = [('Alice', 'HR', 30), ('Bob', 'Engineering', 25), ('Charlie', 'HR', 35)]
sorted_employees = sorted(employees, key=lambda x: (x[1], x[2]))
print(sorted_employees)