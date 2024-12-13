gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
result = gcd(36, 60)
print(result)