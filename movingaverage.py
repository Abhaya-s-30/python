moving_average = lambda nums, n: [sum(nums[i:i+n]) / n for i in range(len(nums) - n + 1)]
result = moving_average([10, 20, 30, 40, 50], 3)
print(result)