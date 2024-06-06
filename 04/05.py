# Считываем шесть чисел
numbers = []
for _ in range(6):
    number = int(input())
    if number != 0:
        numbers.append(number)
product = 1
for number in numbers:
    product *= number
print(product)
