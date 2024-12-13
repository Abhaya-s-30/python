dict1={'apple':20,'orange':5,'blueberry':10}
dict2={'custardapple':25,'orange':5,'blueberry':10}
merge=lambda d1,d2:{**d1,**d2}
result=merge(dict1,dict2)
print(result)