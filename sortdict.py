value={'apple':20,'orange':5,'blueberry':10}
sort=dict(sorted(value.items(),key=lambda item:item[1]))
print(sort)