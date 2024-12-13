numbers=[1,2,3,4,5,6,9,12,15,16,17,30]
divisible_by_3=list(filter(lambda x:x%3==0,numbers))
print(f"numbers divisible by 3: {divisible_by_3}")