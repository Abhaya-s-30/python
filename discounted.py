discounted_price = lambda price, discount: price * (1 - discount / 100)
result = discounted_price(100, 20)
print(result)