num={1,2,3,4,5}
print(num)
element_to_remove=5
if element_to_remove in num:
    num.remove(element_to_remove)
    print(f"after removing {element_to_remove}:",num)
else:
    print(f"{element_to_remove}does not exist")