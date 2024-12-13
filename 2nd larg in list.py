list=[1,4,8,7,5,9]
second_large=lambda list:sorted(set(list))[-2]
result=second_large(list)
print(result)