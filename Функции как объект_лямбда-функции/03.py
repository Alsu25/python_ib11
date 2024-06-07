numbers = filter(lambda x: x % 9 == 0, range(10, 100))
squares = map(lambda x: x ** 2, numbers)
result = sum(squares)
print(result)